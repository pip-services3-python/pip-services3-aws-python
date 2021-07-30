# -*- coding: utf-8 -*-
from pip_services3_commons.refer import Descriptor
from pip_services3_components.build import Factory

from test.DummyController import DummyController
from test.services.DummyCommandableLambdaService import DummyCommandableLambdaService
from test.services.DummyLambdaService import DummyLambdaService


class DummyFactory(Factory):
    DescriptorDummy = Descriptor("pip-services-dummies", "factory", "default", "default", "1.0")
    ControllerDescriptor = Descriptor("pip-services-dummies", "controller", "default", "*", "1.0")
    LambdaServiceDescriptor = Descriptor("pip-services-dummies", "service", "lambda", "*", "1.0")
    CmdLambdaServiceDescriptor = Descriptor("pip-services-dummies", "service", "commandable-lambda", "*", "1.0")

    def __init__(self):
        super().__init__()
        self.register_as_type(DummyFactory.ControllerDescriptor, DummyController)
        self.register_as_type(DummyFactory.LambdaServiceDescriptor, DummyLambdaService)
        self.register_as_type(DummyFactory.CmdLambdaServiceDescriptor, DummyCommandableLambdaService)
