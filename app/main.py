import docker
import time

from common import from_host, docker_sock
from functions import FUNCTIONS

docker_client: docker.DockerClient = docker.DockerClient(base_url=docker_sock())

INTERVAL = 5
LABEL_PREFIX = "dockerauto."


def is_managed(container):
  return any(map(lambda label: label.startswith(LABEL_PREFIX), container.labels))


def execute_all_functions(container):
  results = []

  print(f"{container.id} ({container.name})")
  for label in container.labels:
    if label.startswith(LABEL_PREFIX):
      function = label[len(LABEL_PREFIX):]
      parameter = container.labels[label]
      if function in FUNCTIONS:
        results.append(FUNCTIONS[function](parameter))
        print(f"  {function} {parameter} => {results[-1]}")
      else:
        print(f"Container {container.id} ({container.name}) has an unknown function: {function}")

  return any(results) if len(results) > 0 else True


def cycle():
  containers = docker_client.containers.list(all=True)
  for container in containers:
    if is_managed(container):
      should_be_running = execute_all_functions(container)
      is_running = container.status == "running"
      
      if should_be_running and not is_running:
        print(f"Starting container: {container.id} ({container.name})")
        container.start()
      elif not should_be_running and is_running:
        print(f"Stopping container: {container.id} ({container.name})")
        container.stop()

  
while True:
  cycle()
  time.sleep(INTERVAL)
