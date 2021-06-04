"""This module holds the complete information model for the scienwriter application.
"""

from sciencewriter.informationmodel import CoreConcept, AuthorInfo, SciencePaper, Bibliography, \
             BiblioReference, Note, Argument, Claim, Reason, Evidence, Warrant


class AuthorInfoFindings(CoreConcept): pass
class SciencePaperFindings(CoreConcept): pass
class BibliographyFindings(CoreConcept): pass
class BiblioReferenceFindings(CoreConcept): pass
class NoteFindings(CoreConcept): pass
class ArgumentFindings(CoreConcept): pass
class ClaimFindings(CoreConcept): pass
class ReasonFindings(CoreConcept): pass
class EvidenceFindings(CoreConcept): pass
class WarrantFindings(CoreConcept): pass


class Analyzer():
    """This class provides the functions to verify the internal consistency of the argumentation model.

    It looks at each of the information element instances separately and also to the relevant relations between the information element instances.
    """
    def __init__(self, sciencepaper, bibliography) -> None:
        self.sciencepaper:SciencePaper = sciencepaper
        self.bibliography:Bibliography = bibliography
        pass

    def analyze_science_paper(self, science_paper:SciencePaper) -> SciencePaperFindings:
        """Asserts that the paper has all the author information accounted for and it will then proceed with the verification of all its components.

        Args:
            science_paper (SciencePaper): [description]
        """
        pass

    def analyze_author_info(self, author_info:AuthorInfo) -> AuthorInfoFindings:
        """Asserts that the authors are defined in the bibliography of the application.

        Args:
            author_info (AuthorInfo): The author that needs to be verified
        """
        pass
    
    def analyze_bibliography(self, bibliography:Bibliography) -> BibliographyFindings:
        """Asserts that all authors appear only once in the bibliography of the application.

        Args:
            bibliography (Bibliography): [description]
        """
        pass
    
    def analyze_biblio_reference(self, biblio_reference:BiblioReference) ->BiblioReferenceFindings:
        """Asserts that the biblio reference occurs in the bibliography.

        Args:
            biblio_reference (BiblioReference): [description]
        """
        pass
    
    def analyze_note(self, note:Note) -> NoteFindings:
        """Asserts that a given note has a reference to at least one core concept instance, which may be the paper, the bibliograph or the application itself.

        Args:
            note (Note): [description]
        """
        pass
    
    def analyze_argument(self, argument:Argument) -> ArgumentFindings:
        """Asserts that all the upper level core concepcts of the argument are accounted for and have valid content. This concerns the initial claim, andy supporting reason and evidence relations and a completed conclusion discussion.

        Args:
            argument (Argument): [description]
        """
        pass
    
    def analyze_claim(self, claim:Claim) -> ClaimFindings:
        """Asserts that the claim is either the initial claims or that it is correctly associated with one of the used reasons in the argument.

        Args:
            claim (Claim): [description]
        """
        pass
    
    def analyze_reason(self, reason:Reason) -> ReasonFindings:
        """Asserts that the reason is correctly associated with a claim; whether it is an initial claim or one of the core concepts that functions as a claim elsewhere in the argumentation model, such as: warrants. To be complete the reason must be suppored by (at least two) valid statements of evidence.

        Args:
            reason (Reason): [description]
        """
        pass
    
    def analyze_evidence(self, evidence:Evidence) -> EvidenceFindings:
        """Asserts that the evidence is associated with at least on statement of reasoning. The evidence as always supported by at least one external bibliographical reference or communication note that stands for an external reference.

        Args:
            evidence (Evidence): [description]
        """
        pass
    
    def analyze_warrant(self, warrant:Warrant) -> WarrantFindings:
        """Asserts that the warrant has all the components that make up the general/specific jsutification accounted for. Some components of the warrant have dual roles; both inside and outside the warrant model. When the general reason/claims can serve as their own core concepts.

        Args:
            warrant (Warrant): [description]
        """
        pass
