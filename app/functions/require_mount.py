from common import from_host

def require_mount(path):
  with open(from_host("/proc/mounts")) as mounts:
    mounts = mounts.readlines()
  mounted = map(lambda x: x.split(" ")[1], mounts)
  return any(map(lambda x: x == from_host(path), mounted))


EXPORTED_FUNCTIONS = {
  "require-mount": require_mount,
}