# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
import pulumi_azure_native

__all__ = ['ContainerappArgs', 'Containerapp']

@pulumi.input_type
class ContainerappArgs:
    def __init__(__self__, *,
                 docker_image_name: Optional[pulumi.Input[str]] = None,
                 image_directory: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 registry: Optional[pulumi.Input['pulumi_azure_native.containerregistry.Registry']] = None,
                 resource_group: Optional[pulumi.Input['pulumi_azure_native.resources.ResourceGroup']] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Containerapp resource.
        :param pulumi.Input[str] docker_image_name: The name of the docker image to use. Required. Either this or imageDirectory must be provided. A docker image will be created if this is not provided.
        :param pulumi.Input[str] image_directory: The relative directory path to the folder containing the docker image. Either this or dockerImageName must be provided.
        :param pulumi.Input[str] name_prefix: The name prefix given to child resources of this component. Should not contain dashes.
        :param pulumi.Input['pulumi_azure_native.containerregistry.Registry'] registry: The container registry to use. One will be created if not provided.
        :param pulumi.Input['pulumi_azure_native.resources.ResourceGroup'] resource_group: The resource group to use. One will be created if not provided.
        :param pulumi.Input[str] version: The version of the docker image created, if not provided
        """
        if docker_image_name is not None:
            pulumi.set(__self__, "docker_image_name", docker_image_name)
        if image_directory is not None:
            pulumi.set(__self__, "image_directory", image_directory)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if registry is not None:
            pulumi.set(__self__, "registry", registry)
        if resource_group is not None:
            pulumi.set(__self__, "resource_group", resource_group)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="dockerImageName")
    def docker_image_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the docker image to use. Required. Either this or imageDirectory must be provided. A docker image will be created if this is not provided.
        """
        return pulumi.get(self, "docker_image_name")

    @docker_image_name.setter
    def docker_image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "docker_image_name", value)

    @property
    @pulumi.getter(name="imageDirectory")
    def image_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The relative directory path to the folder containing the docker image. Either this or dockerImageName must be provided.
        """
        return pulumi.get(self, "image_directory")

    @image_directory.setter
    def image_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_directory", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The name prefix given to child resources of this component. Should not contain dashes.
        """
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter
    def registry(self) -> Optional[pulumi.Input['pulumi_azure_native.containerregistry.Registry']]:
        """
        The container registry to use. One will be created if not provided.
        """
        return pulumi.get(self, "registry")

    @registry.setter
    def registry(self, value: Optional[pulumi.Input['pulumi_azure_native.containerregistry.Registry']]):
        pulumi.set(self, "registry", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input['pulumi_azure_native.resources.ResourceGroup']]:
        """
        The resource group to use. One will be created if not provided.
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input['pulumi_azure_native.resources.ResourceGroup']]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the docker image created, if not provided
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Containerapp(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 docker_image_name: Optional[pulumi.Input[str]] = None,
                 image_directory: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 registry: Optional[pulumi.Input['pulumi_azure_native.containerregistry.Registry']] = None,
                 resource_group: Optional[pulumi.Input['pulumi_azure_native.resources.ResourceGroup']] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Containerapp resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] docker_image_name: The name of the docker image to use. Required. Either this or imageDirectory must be provided. A docker image will be created if this is not provided.
        :param pulumi.Input[str] image_directory: The relative directory path to the folder containing the docker image. Either this or dockerImageName must be provided.
        :param pulumi.Input[str] name_prefix: The name prefix given to child resources of this component. Should not contain dashes.
        :param pulumi.Input['pulumi_azure_native.containerregistry.Registry'] registry: The container registry to use. One will be created if not provided.
        :param pulumi.Input['pulumi_azure_native.resources.ResourceGroup'] resource_group: The resource group to use. One will be created if not provided.
        :param pulumi.Input[str] version: The version of the docker image created, if not provided
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ContainerappArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Containerapp resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ContainerappArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerappArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 docker_image_name: Optional[pulumi.Input[str]] = None,
                 image_directory: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 registry: Optional[pulumi.Input['pulumi_azure_native.containerregistry.Registry']] = None,
                 resource_group: Optional[pulumi.Input['pulumi_azure_native.resources.ResourceGroup']] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerappArgs.__new__(ContainerappArgs)

            __props__.__dict__["docker_image_name"] = docker_image_name
            __props__.__dict__["image_directory"] = image_directory
            __props__.__dict__["name_prefix"] = name_prefix
            __props__.__dict__["registry"] = registry
            __props__.__dict__["resource_group"] = resource_group
            __props__.__dict__["version"] = version
            __props__.__dict__["url"] = None
        super(Containerapp, __self__).__init__(
            'azure-justrun:index:containerapp',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "url")
