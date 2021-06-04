"""This module holds the complete information model for the scienwriter application.
"""

import uuid
class ScienceWriterApp():
    """This class represents the application as a whole that exposes the API for other derived works to access and to manipulate the internals of the writing project.
    """
    def __init__(self) -> None:
        self.papers:list[SciencePaper] = None
        self.location:str = None
        self.author_infos:dict[str,AuthorInfo] = None
        pass


class CoreConcept():
    """This class represents common properties and functions that are used/apply to all information entities in the application. Mostly concerns identity properties for internal references in the application.
    """
    def __init__(self) -> None:
        self.guuid = uuid.uuid4()
        self.notes:list[Note] = []
        pass


class AuthorInfo(CoreConcept):
    """This class maintains information about an author in the application.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.call_name:str = None
        self.middle_initials:str = None
        self.family_name:str = None
        self.contact_email:str = None
        self.contact_webpage:str = None
    

class SciencePaper(CoreConcept):
    """This class represents the context for writing a single paper. This concerns everything about the argumentation model as well as all the external bibliographic references and notes taken during the writing process.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.argument:Argument = None        
        self.bibliography:Bibliography = None
        self.authors:list[AuthorInfo] = []
    pass


class Bibliography(CoreConcept):
    """This class represents the full collection of external references that are used as evidence in the argumentation model or serve as backkground information during the exploratory phase of the writing process. A single author can appear multiple times in the collection but not with the same information; eg different years that its properties were relevant or different institutions at a given moment in time. The info-record is sequential for an author's famname+callname

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.references:dict[str,BiblioReference] = []
        pass


class BiblioReference(CoreConcept):
    """This class represents a single bibliographic reference to some source document that is used as part of the evidence in the argumentation model.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.unique_ref:str = None
        self.title:str = None
        self.journal:str = None
        self.pages:str = None
        self.url:str = None
        self.authors:list[str] = []
    pass


class Note(CoreConcept):
    """This class represents a single note-2-self that is applied to a specific core concept to make a reminder or some comment on the specific item.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.text:str = None
        self.core_concepts:list[CoreConcept] = []
    pass


class Argument(CoreConcept):
    """This class represents a single argument in the whole argumentation structure. The argument is the outer-container for the BCW argumentation model.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.introductory_claim:Claim = None
        self.claims:list[Claim] = []
    pass


class Claim(CoreConcept):
    """This class represents a single claim in the argumentation model. Claims can exist on several levels depending on their target in the model.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.text:str = None
        self.reasons:list[Reason] = []
    pass


class Reason(CoreConcept):
    """This class represents a reason that explains why the claim it relates to is relevant to the argumentation for the paper.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.text:str = None
        self.evidences:list[Evidence] = []
    pass


class Evidence(CoreConcept):
    """This class represents a single element of evidence that is supportive of the claim(s) it relates to. A single element of evidence can be supported in multiple locations in the argumentation model. Evidence is always supported by external source references.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.text:str = None
        self.sources:list[BiblioReference] = []
    pass


class Warrant(CoreConcept):
    """This class represents a single warrant for the argumentation model and it is defined by its four components and the justification/explanation of the relevance to the claim/reason instance it refers to.

    The warrant model is that based on a general claim that we can agree on has a general consequence the warrant shows that of our reason is a valid specific instance of the general case we can infer the specific claim if we agree it is a valid instance of the general consequence.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.reason:Reason = None
        self.claim:Claim = None
        self.general_claim:Reason = None
        self.general_consequence:Claim = None
        self.reason:Reason = None
        self.reason:Claim = None
        self.text:str = None
    pass


class Conclusion(CoreConcept):
    """This class represents the overall conclusion for the science paper that relates to the intial claim of the paper.

    Args:
        CoreConcept ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.claim:Claim = None
        self.conclusion:str = None
    pass

