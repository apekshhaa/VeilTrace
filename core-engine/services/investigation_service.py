# from models.investigation import Investigation


# class InvestigationService:

#     def start_investigation(
#         self,
#         name: str,
#         target: str,
#     ) -> Investigation:

#         return Investigation(
#             name=name,
#             target=target,
#         )

#     def close_investigation(self):
#         pass

#     def update_status(self):
#         pass
from models.investigation import Investigation


class InvestigationService:

    def __init__(self):
        self.current = None

    def start(self, name: str, target: str):

        self.current = Investigation(
            name=name,
            target=target,
        )

        return self.current

    def get(self):

        return self.current

    def complete(self):

        if self.current:
            self.current.status = "COMPLETED"

        return self.current