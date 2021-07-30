# -*- coding: utf-8 -*-
from typing import Optional

from pip_services3_commons.commands import CommandSet, ICommand, Command
from pip_services3_commons.convert import TypeCode
from pip_services3_commons.data import FilterParams, PagingParams
from pip_services3_commons.run import Parameters
from pip_services3_commons.validate import ObjectSchema, FilterParamsSchema, PagingParamsSchema

from test.Dummy import Dummy
from test.DummySchema import DummySchema
from test.IDummyController import IDummyController


class DummyCommandSet(CommandSet):

    def __init__(self, controller: IDummyController):
        super(DummyCommandSet, self).__init__()

        self.__controller: IDummyController = controller

        self.add_command(self.__make_get_page_by_filter_command())
        self.add_command(self.__make_get_one_by_id_command())
        self.add_command(self.__make_create_command())
        self.add_command(self.__make_update_command())
        self.add_command(self.__make_delete_by_id_command())

    def __make_get_page_by_filter_command(self) -> ICommand:
        def command_func(correlation_id: Optional[str], args: Parameters):
            filter = FilterParams.from_value(args.get("filter"))
            paging = PagingParams.from_value(args.get("paging"))
            return self.__controller.get_page_by_filter(correlation_id, filter, paging)

        return Command(
            "get_dummies",
            ObjectSchema(True).with_optional_property("filter", FilterParamsSchema())
                .with_optional_property("paging", PagingParamsSchema()),
            command_func
        )

    def __make_get_one_by_id_command(self) -> ICommand:
        def command_func(correlation_id: Optional[str], args: Parameters):
            id = args.get_as_string("dummy_id")
            return self.__controller.get_one_by_id(correlation_id, id)

        return Command(
            "get_dummy_by_id",
            ObjectSchema(True).with_required_property("dummy_id", TypeCode.String),
            command_func
        )

    def __make_create_command(self) -> ICommand:
        def command_func(correlation_id: Optional[str], args: Parameters):
            entity: Dummy = args.get("dummy")
            return self.__controller.create(correlation_id, entity)

        return Command(
            "create_dummy",
            ObjectSchema(True).with_required_property("dummy", DummySchema()),
            command_func
        )

    def __make_update_command(self) -> ICommand:
        def command_func(correlation_id: Optional[str], args: Parameters):
            entity: Dummy = args.get("dummy")
            return self.__controller.update(correlation_id, entity)

        return Command(
            "update_dummy",
            ObjectSchema(True).with_required_property("dummy", DummySchema()),
            command_func
        )

    def __make_delete_by_id_command(self) -> ICommand:
        def command_func(correlation_id: Optional[str], args: Parameters):
            id = args.get_as_string("dummy_id")
            return self.__controller.delete_by_id(correlation_id, id)

        return Command(
            "delete_dummy",
            ObjectSchema(True).with_required_property("dummy_id", TypeCode.String),
            command_func
        )
