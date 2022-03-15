# Docker Auto

This is a very simple automation tool for Docker containers. It its focused on being modular and simple to extend and use. Currently there are a very limited of functions implemented, but this can be later expanded based on my personal demand.

# Usage

A function "call" is declared by the Docker Auto prefix (`dockerauto`) followed by a dot and the function name. For example, a call to the _Require Mount_ function is `dockerauto.require-mount`. The parameter for such function is the required path to be mounted. Function "calls" are defined by _labels_ in the container. As such, an usage example for this function would be the following:

```
dockerauto.require-mount=/mnt
```

# Functions

A function is a simple python function that will be called with the label's value and must return `True` or `False`. This will later be used to figure out if the container should be or not running. The idea is that such functions will allow the container to be stopped or started dynamically based on some external requirement, such as current time, host mounts, etc.

These are the available functions:

## Require Mount

This function will check if a specific destination is mounted on the host OS. Keep in mind this function will require access to host information for it to work properly. This can be done through the `privileged` flag, or passing the root filesystem as a volume into the container.

- Name: `dockerauto.require-mount`
- Parameter: required path to be mounted
- Requirements: `HOST_PREFIX` + mounted host root

Example:

```
version: '3'
services:
  dockerauto:
    container_name: dockerauto
    volumes:
      - /:/host:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
      - HOST_PREFIX=/host
      - DOCKER_SOCK=unix://var/run/docker.sock
    build: .
```

In this example, everything pointing to the root filesystem will be prefixed with `/host`. As such, reading `/proc/mounts` will actually read `/host/proc/mounts`, which even in unprivileged containers will provide the host mounts, along the container ones. There are probably better solutions to this problem, but this is the one I've managed to find so far. For safety reasons, the host container is provided as read-only.

# Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

TL;DR: if this breaks something, it's your own fault. Sorry.