# _ITU-MiniTwit_ Simulator API with OpenAPI Specification

## What is the OpenAPI Specification (previously Swagger)?

> The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to HTTP APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection. [...]
>
> An OpenAPI Description can then be used by documentation generation tools to display the API, code generation tools to generate servers and clients in various programming languages, testing tools, and many other use cases.
>
> https://swagger.io/specification/

The [OpenAPI Generator](https://openapi-generator.tech/) is a tool that takes an Open API document (an interface specification) written in the OpenAPI JSON format and automatically generates boilerplate code for you.
It can do so for both sides of a client-server application.
That is, it can automatically generates server stubs (controllers/routes) and client SDKs (HTTP callers).
Additionally, it can generate documentation.
In the following, we use the OpenAPI Generator to generate the stub of an _ITU-MiniTwit_ Simulator API HTTP server application.


## How to install the OpenAPI Generator CLI tool?

You can find installation documentation [here](https://openapi-generator.tech/docs/installation).
There are several ways to install the OpenAPI Generator CLI tool.
You can install the tool directly to your development computer.
However, then you have to install a lot of dependencies, which might be tricky since it depends on Java and a lot of Java tooling.
Therefore, we focus on using the OpenAPI Generator CLI tool packaged and usable via a Docker container.

If you would like to try other ways, you can visit the website.


## How to use the OpenAPI Generator CLI tool?

## Step 00: Navigate to your _ITU-MiniTwit_ application directory

```bash
cd ~/<path_to>/itu-minitwit
```

### Step 01: Get the Open API Interface Specification JSON file (swagger3.json)

You can find the Open API Interface Specification JSON file for our project [here](./swagger3.json).
This file specifies the contract between the _ITU-MiniTwit_ Simulator and your _ITU-MiniTwit_ Simulator API application.
It contains the exact definitions for every endpoint, input, and output your API must support.
The OpenAPI Generator CLI tool consumes this file to automatically generate a stub of your _ITU-MiniTwit_ Simulator API application.

Copy this file to the root of your _ITU-MiniTwit_ application directory:

```bash
cp ~/<path_to_lecture_notes>/sessions/session_03/API_Spec/swagger3.json .
```

### Step 02: Use the OpenAPI Generator CLI tool to generate a stub application

**OBS**: This guide requires you to have the Docker command line tool `docker` installed and setup.
If you do not have it installed yet, check the [preparation material of last week's session](../../session_02/READMDE_PREP.md)


Within the root directory of your _ITU-MiniTwit_ application directory, i.e., a directory containing the `swagger3.json` file, run the following command to generate generate a stub of an _ITU-MiniTwit_ Simulator API application.

```bash
docker run --rm -v "$(pwd):/local" openapitools/openapi-generator-cli:v7.19.0 \
  generate \
  -i /local/swagger3.json \
  -g aspnetcore \
  -o /local/out/itu-minitwit-sim-stub \
  --additional-properties=buildTarget=program,aspnetCoreVersion=8.0,operationIsAsync=true,nullableReferenceTypes=true,useSwashbuckle=true
```

**Optional reading**: What does this command do?
  - It calls the `docker` CLI tool with the `run` command, which creates and runs a new container from an image, see `docker run -h`
  - `--rm` flag ensures that the container is cleaned-up and removed after completion of the containerized process. In other words: it tells `docker` _please remove and clean up this container, once a stub application is generated_.
  - `-v` mount a volume, i.e., a directory from your host computer into the container. Here, we mount the current working directory the the directory `/local` in the container. If in doubt, read the manual page of the `pwd` command.
  - `openapitools/openapi-generator-cli:v7.19.0` is a pinned version of the OpenAPI Generator CLI tool's docker image (namely version `v7.19.0`).
  - `generate` is the argument given to the containerized `openapi-generator-cli` command, which is executed within the container. See the [documentation](https://openapi-generator.tech/docs/usage) for other arguments. It means _"Generate code with the specified generator"_. The respective code generator is specified with the argument to the `-g` flag.
  - The argument to `-i` (_input_) flag points to the path of the Open API specification file within the container, here `/local/swagger3.json`
  - The argument to the `-g` flag specifies the language/framework in which the stub application shall be created. Here, it is `aspnetcore` which generates a C♯/.Net application. Find a list of alternative generators [here](https://openapi-generator.tech/docs/generators/).
  - The argument to the `-o` specifies the output path to which the stub application is written. Here it is `/local/out/itu-minitwit-sim-stub` within the container, which maps to `$(pwd)/out/itu-minitwit-sim-stub` on your host machine.
  - Finally, we provide some additional properties (`--additional-properties`) to the code generator. Here you modify the structure and behavior of the generated stub application. A complete list of configurable properties is available [here](https://openapi-generator.tech/docs/generators/aspnetcore/).

After you run this command, you will find generated solution under `out/`.
The generated stub application contains a Dockerfile so you can build and run the application directly in a docker container.
⚠️ Note however, that the generated Dockerfile refers to a deprecated base image.

If `docker build` fails, you **must** manually fix the `Dockerfile` by replacing the references to the deprecated base image with references to an existing one.
For example, replace `FROM mcr.microsoft.com/dotnet/core/aspnet:8.0-buster-slim AS base` with `FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base` or `FROM mcr.microsoft.com/dotnet/core/sdk:8.0-buster AS build` with `FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build`.

Now, you can build a Docker image for your stub application and run it.
If in doubt refer to last week's exercise material


Once you have a running container with a stub an _ITU-MiniTwit_ Simulator API application, you can run a basic simulator against it.
Together with this week's lecture material, we provide you a [basic simulator](./minitwit_simulator.py).

```bash
$ python minitwit_simulator.py http://<url_of_your_containerized_itu_minitwit_sim_api>
```

When running the simulator against the generated stub an _ITU-MiniTwit_ Simulator API application, you will observe a lot of "not implemented" exceptions in its logs and endpoints that return a 501 HTTP status code.
You have to complete the implementation of the generated _ITU-MiniTwit_ Simulator API application by integrating it into your _ITU-MiniTwit_ application and by implementing the respective HTTP handler methods.
