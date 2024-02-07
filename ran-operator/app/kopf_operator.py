import kopf
import datetime
import random
import logging


@kopf.on.probe(id='now')
def get_current_timestamp(**kwargs):
    return datetime.datetime.utcnow().isoformat()

@kopf.on.probe(id='random')
def get_random_value(**kwargs):
    return random.randint(0, 1_000_000)

# When creating or resuming object
@kopf.on.resume('ranoperator.example.com', 'v1alpha1', 'ranoperator')
@kopf.on.create('ranoperator.example.com', 'v1alpha1', 'ranoperator')
def create_fn(spec, name, namespace, logger, **kwargs):
    logger.info(f"Creating: {spec}")
    data = hello_world(spec, name)
    logger.info(data)
  
@kopf.on.update('ranoperator.example.com', 'v1alpha1', 'ranoperator')
def modify_fn(spec, name, namespace, logger, **kwargs):
    logger.info(f"Modifying: {spec}")
    data = hello_world(spec, name)
    logger.info(data)

@kopf.on.delete('ranoperator.example.com', 'v1alpha1', 'ranoperator')
def delete_fn(spec, name, logger, **kwargs):
    logger.info(f"Deleting: {spec}")
    
def hello_world(spec, name):
    logging.info(f"Hello World: {spec}")
    logging.info(f"Hello World: {name}")
    return {'hello': 'world'}


