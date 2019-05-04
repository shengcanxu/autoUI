from pywinauto.application import WindowSpecification

class GetMultipleObjectsException(Exception):

    """gets more than one object from the filters"""
    pass    # pragma: no cover

class GetNoObjectException(Exception):

    """gets no object from the filters"""
    pass    # pragma: no cover


class ElementInfoWrapper(object):

    def __init__(self,app, elements = None):
        self._app = app
        if type(self._app.WINDOWRECT) == WindowSpecification:
            rect = self._app.window().wrapper_object().rectangle()
            self._app.__setattr__("WINDOWRECT",rect)

        if elements is None:
            self._elements = app.windows()
        else:
            self._elements = elements

    def getElements(self):
        return self._elements

    def length(self):
        return len(self._elements)

    def getParent(self):
        clone = self._elements.copy()
        parents = []

        for elem in clone:
            parent = elem.parent
            if parent is not None:
                parents.append(parent)

        if len(parents) == 0:
            raise Exception("no parents found!")

        return ElementInfoWrapper(self._app, parents)

    def filter(self, **criteria):
        elements = self._elements.copy()
        elements = self._filter(elements,**criteria)
        return ElementInfoWrapper(self._app,elements)

    def filterDecendent(self, **criteria):
        clone = self._elements.copy()
        elements = []

        for elem in clone:
            children = elem.children()
            if len(children) >  0:
                newElements = self._filter(children,**criteria)
                elements.extend(newElements)

        return ElementInfoWrapper(self._app, elements)

    def filterChildren(self, **criteria):
        clone = self._elements.copy()
        elements = []

        for elem in clone:
            children = elem.children()
            if len(children) > 0:
                criteria["recursion"] = False
                newElements = self._filter(children, **criteria)
                elements.extend(newElements)

        return ElementInfoWrapper(self._app, elements)

    def filterTop(self, **criteria):
        elements = self._elements.copy()
        criteria["recursion"] = False
        elements = self._filter(elements, **criteria)
        return ElementInfoWrapper(self._app, elements)

    def _filter(self, elements,
                class_name=None,
                control_type=None,
                text=None,
                index=None,
                children_num=None,
                contain_point=None,
                recursion=True):
        if elements is None or len(elements) == 0:
            return []

        clone = elements.copy()

        if class_name is not None and len(elements)>0:
            elements = [elem for elem in elements if elem.class_name == class_name]

        if control_type is not None and len(elements)>0:
            elements = [elem for elem in elements if elem.control_type == control_type]

        if text is not None and len(elements)>0:
            elements = [elem for elem in elements if elem.rich_text == text]

        if children_num is not None and len(elements)>0:
            elements = [elem for elem in elements if len(elem.children()) == children_num]

        if contain_point is not None and len(elements)>0:
            def _contain_point(rect,point):
                if (rect.left-self._app.WINDOWRECT.left) <= point[0] and (rect.right-self._app.WINDOWRECT.left) >=point[0] and \
                        (rect.top-self._app.WINDOWRECT.top) <=point[1] and (rect.bottom--self._app.WINDOWRECT.top) >= point[1]:
                    return True
                else:
                    return False

            elements = [elem for elem in elements if _contain_point(elem.rectangle, contain_point)]

        if index is not None :
            if len(elements) >= index:
                elements = [elements[index-1]]
            else:
                elements = []

        if recursion:
            for elem in clone:
                children = elem.children()
                if len(children) >  0:
                    newElements = self._filter(children,
                                               class_name,
                                               control_type,
                                               text,
                                               index,
                                               children_num,
                                               contain_point,
                                               recursion)
                    elements.extend(newElements)

        return elements

    def _getObject(self,index):
        if len(self._elements) <= 0 :
            raise GetNoObjectException("no objects from filters, please refine filters")

        return self._app.backend.generic_wrapper_class(self._elements[index])

    def getObject(self):
        if len(self._elements) > 1 :
            self.dump(prefix="",elements=self._elements)
            raise GetMultipleObjectsException("more than one objects from filters, please refine fiters")
        return self._getObject(0)

    def getAllObjects(self):
        return [self._app.backend.generic_wrapper_class(elem) for elem in self._elements]

    def getFirstObject(self):
        return self._getObject(0)

    def getLastObject(self):
        return self._getObject(-1)

    def exist(self):
        return len(self._elements) > 0

    def dump(self, prefix="",elements=None):
        if elements is None:
            elements = self._elements
        for elem in elements:
            print(prefix, end=">")
            print(elem.class_name,end=":")
            print(elem.control_type, end=":")
            print(elem.rich_text, end=" ")
            print(elem.rectangle)
            self.dump(prefix + "    ", elem.children() )
