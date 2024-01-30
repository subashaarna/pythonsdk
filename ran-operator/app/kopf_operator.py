import kopf

# When creating or resuming object
@kopf.on.resume('example.com', 'v1alpha1', 'ran')
@kopf.on.create('example.com', 'v1alpha1', 'ran')
def create_fn(spec, name, namespace, logger, **kwargs):
    print(f"Creating: {spec}")
    data = hello_world(spec, name)
    print(data)
  

@kopf.on.delete('example.com', 'v1alpha1', 'ran')
def delete_fn(spec, name, status, namespace, logger, **kwargs):
    print(f"Deleting: {spec}")
    
def hello_world(spec, name):
    print(f"Hello World: {spec}")
    print(f"Hello World: {name}")
    return {'hello': 'world'}