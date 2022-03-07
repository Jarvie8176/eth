from __future__ import annotations

from typing import List, Dict

from dto.TronGrid.transaction import TrxDto
from models.exceptions import ParserNotFound
from parser.TronGrid.parserDefn import parser_list
from parser.base import BaseParser


class ParserLookup:
    def __init__(self) -> None:
        self.parsers: Dict[int, List[BaseParser]] = {}
        """
        :param parsers: a kv pair of priority and a list of parsers of that priority
        """

    def add_parser(self, parser: BaseParser) -> ParserLookup:
        priority = parser.load_order
        if not self.parsers.get(priority):
            self.parsers[priority] = []

        priority_list = self.parsers[priority]
        priority_list.append(parser)
        return self

    def find_parser(self, trx: TrxDto) -> BaseParser:
        for priority in self.parsers.keys():
            try:
                return next(parser for parser in self.parsers.get(priority) or [] if parser.can_handle(trx))
            except StopIteration:
                continue
        raise ParserNotFound()

    @staticmethod
    def create() -> ParserLookup:
        parser_lookup = ParserLookup()

        for parser in parser_list:
            parser_lookup.add_parser(parser)

        return parser_lookup
