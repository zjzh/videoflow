from videoflow.core import Flow
from videoflow.producers import IntProducer
from videoflow.processors import IdentityProcessor, JoinerProcessor
from videoflow.consumers import CommandlineConsumer

producer = IntProducer(0, 40, 0.1)
identity = IdentityProcessor(fps = 2, nb_tasks = 2, name = 'i1')(producer)
identity1 = IdentityProcessor(fps = 2, nb_tasks = 2, name = 'i2')(identity)
joined = JoinerProcessor(nb_tasks = 5)(identity, identity1)
printer = CommandlineConsumer()(joined)
flow = Flow([producer], [printer])
flow.run()
flow.join()
