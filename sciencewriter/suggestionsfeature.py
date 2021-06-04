"""This module holds the complete information model for the scienwriter application.
"""

from sciencewriter.informationmodel import CoreConcept, AuthorInfo, SciencePaper, Bibliography, \
            BiblioReference, Note, Argument, Claim, Reason, Evidence, Warrant


from sciencewriter.analysisfeature import AuthorInfoFindings, BibliographyFindings, \
            BiblioReferenceFindings, NoteFindings, ArgumentFindings, ClaimFindings, \
            ReasonFindings, EvidenceFindings, WarrantFindings, SciencePaperFindings 


class Editor():
    """This class takes in the analysis findings and will generate suggestions based on the findings that came out of the analyzer feature.
    """
    def __init__(self, sciencepaper, bibliography) -> None:
        self.sciencepaper:SciencePaper = sciencepaper
        self.bibliography:Bibliography = bibliography
        pass

    def editsuggest_science_paper(self, finding:SciencePaperFindings):
        """Asserts that the paper has all the author information accounted for and it will then proceed with the verification of all its components.

        Args:
            science_paper (SciencePaper): [description]
        """
        pass

    def editsuggest_author_info(self, finding:AuthorInfoFindings):
        """Asserts that the authors are defined in the bibliography of the application.

        Args:
            author_info (AuthorInfo): The author that needs to be verified
        """
        pass
    
    def editsuggest_bibliography(self, finding:BibliographyFindings):
        """Asserts that all authors appear only once in the bibliography of the application.

        Args:
            bibliography (Bibliography): [description]
        """
        pass
    
    def editsuggest_biblio_reference(self, finding:BiblioReferenceFindings):
        """Asserts that the biblio reference occurs in the bibliography.

        Args:
            biblio_reference (BiblioReference): [description]
        """
        pass
    
    def editsuggest_note(self, findings:NoteFindings):
        """Asserts that a given note has a reference to at least one core concept instance, which may be the paper, the bibliograph or the application itself.

        Args:
            note (Note): [description]
        """
        pass
    
    def editsuggest_argument(self, findings:ArgumentFindings):
        """Asserts that all the upper level core concepcts of the argument are accounted for and have valid content. This concerns the initial claim, andy supporting reason and evidence relations and a completed conclusion discussion.

        Args:
            argument (Argument): [description]
        """
        pass
    
    def editsuggest_claim(self, findings:ClaimFindings):
        """Asserts that the claim is either the initial claims or that it is correctly associated with one of the used reasons in the argument.

        Args:
            claim (Claim): [description]
        """
        pass
    
    def editsuggest_reason(self, findings:ReasonFindings):
        """Asserts that the reason is correctly associated with a claim; whether it is an initial claim or one of the core concepts that functions as a claim elsewhere in the argumentation model, such as: warrants. To be complete the reason must be suppored by (at least two) valid statements of evidence.

        Args:
            reason (Reason): [description]
        """
        pass
    
    def editsuggest_evidence(self, findings:EvidenceFindings):
        """Asserts that the evidence is associated with at least on statement of reasoning. The evidence as always supported by at least one external bibliographical reference or communication note that stands for an external reference.

        Args:
            evidence (Evidence): [description]
        """
        pass
    
    def editsuggest_warrant(self, findings:WarrantFindings):
        """Asserts that the warrant has all the components that make up the general/specific jsutification accounted for. Some components of the warrant have dual roles; both inside and outside the warrant model. When the general reason/claims can serve as their own core concepts.

        Args:
            warrant (Warrant): [description]
        """
        pass
