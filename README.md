# A dummy Renku workflow provider implementation

This repository contains a simple workflow provider implementation that will extend your renku installation
with a provider called `dummy`. After successfully installing this plugin one should be able to execute
an existing renku workflow with this provider:

```
$ renku workflow execute -p dummy <my_workflow>
```

Note, because of the actual implementation this will not execute the workflow at all, only an error
will be raised by renku.

For more information about the internals of a renku workflow provider please check out the
[Implementing a workflow provider](https://renku.readthedocs.io/projects/renku-python/en/latest/how-to-guides/implementing_a_provider.html#implementing-a-provider)
section of the documentation.
