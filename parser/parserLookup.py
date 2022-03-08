from __future__ import annotations

from typing import Dict, List, Sequence, TypeVar, Generic

from models.exceptions import ParserNotFound
from parser.base import BaseParser

TrxDtoType = TypeVar("TrxDtoType")


class ParserLookup(Generic[TrxDtoType]):
    def __init__(self) -> None:
        self.parsers: Dict[int, List[BaseParser[TrxDtoType]]] = {}
        """
        :param parsers: a kv pair of priority and a list of parsers of that priority
        """

    def add_parser(self, parser: BaseParser[TrxDtoType]) -> ParserLookup[TrxDtoType]:
        priority = parser.load_order
        if not self.parsers.get(priority):
            self.parsers[priority] = []

        priority_list = self.parsers[priority]
        priority_list.append(parser)
        return self

    def find_parser(self, trx: TrxDtoType) -> BaseParser[TrxDtoType]:
        for priority in self.parsers.keys():
            try:
                return next(parser for parser in self.parsers.get(priority) or [] if parser.can_handle(trx))
            except StopIteration:
                continue
        raise ParserNotFound("parser not found")

    @staticmethod
    def from_parser_list(parser_list: Sequence[BaseParser[TrxDtoType]]) -> ParserLookup[TrxDtoType]:
        parser_lookup = ParserLookup[TrxDtoType]()

        for parser in parser_list:
            parser_lookup.add_parser(parser)

        return parser_lookup
