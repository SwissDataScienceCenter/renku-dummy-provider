# An example Renku workflow provider implementation

This repository contains a simple workflow provider implementation that will extend your renku installation
with a provider called `dummy`. 

## Installation

Clone the repository locally and install with `pip` in the same environment as your `renku` CLI installation. 
We recommend using a virtual environment. For example:

```bash
$ pip install virtualenv
$ virtualenv /tmp/renku-new-wf-provider
$ source /tmp/renku-new-wf-provider/bin/activate
$ pip install <path-to-renku-dummy-provider-repo>
```

## Usage

To see if the provider was installed, run 

```
$ renku workflow execute --help
renku workflow execute --help                                                                                                                                                                                                              
Usage: renku workflow execute [OPTIONS] NAME_OR_ID

  Execute a given workflow.

Options:
  -p, --provider [cwltool|dummy]  The workflow engine to use.  [default:
                                  cwltool]
```

You should see `dummy` in the list of providers, as in the above output.

```
$ renku workflow execute -p dummy <my_workflow>
```

Note, because of the actual implementation this will not execute the workflow at all, only an error
will be raised by renku.

For more information about the internals of a renku workflow provider please check out the
[Implementing a workflow provider](https://renku.readthedocs.io/projects/renku-python/en/latest/how-to-guides/implementing_a_provider.html#implementing-a-provider)
section of the documentation.
