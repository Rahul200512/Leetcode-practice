# TIL: Docker 101

Spent some time today learning the absolute basics of Docker, and honestly, it clicks! It's essentially a way to package up an application and all its dependencies into a standard unit called a **container**. Think of it as a really lightweight, isolated environment, almost like a mini-VM, but way faster and more efficient.

The core concepts I got are **Images** and **Containers**. An Image is like a blueprint or a snapshot – it's the read-only template with your app, libraries, configs, etc. A Container is a running instance of that Image. So, I can run multiple containers from the same image.

Running something is surprisingly simple. For example, to just test it out:

```bash
docker run hello-world
docker ps -a # to see finished containers
```

This pulled the `hello-world` image (if not local) and ran it. It’s a game-changer for avoiding "it works on my machine" issues. I can see why people love this for consistent dev environments.
