from dataclasses import dataclass
from typing import Optional, TypedDict, NewType, Dict

from robyn.robyn import Url, Identity


@dataclass
class Directory:
    route: str
    directory_path: str
    show_files_listing: bool
    index_file: Optional[str]

    def as_list(self):
        return [
            self.route,
            self.directory_path,
            self.show_files_listing,
            self.index_file,
        ]


PathParams = NewType("PathParams", Dict[str, str])
RequestMethod = NewType("RequestMethod", str)
RequestURL = NewType("RequestURL", Url)
FormData = NewType("FormData", Dict[str, str])
RequestFiles = NewType("RequestFiles", Dict[str, bytes])
RequestIP = NewType("RequestIP", Optional[str])
RequestIdentity = NewType("RequestIdentity", Optional[Identity])


class JSONResponse(TypedDict):
    pass


class RequestBody:
    pass


class QueryParam:
    pass
