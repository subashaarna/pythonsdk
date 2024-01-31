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
    logging.info(f"Creating: {spec}")
    data = hello_world(spec, name)
    logging.info(data)
  

@kopf.on.delete('ranoperator.example.com', 'v1alpha1', 'ranoperator')
def delete_fn(spec, name, status, namespace, logger, **kwargs):
    logging.info(f"Deleting: {spec}")
    logging.info(f"status {status}")
    
def hello_world(spec, name):
    logging.info(f"Hello World: {spec}")
    logging.info(f"Hello World: {name}")
    return {'hello': 'world'}
