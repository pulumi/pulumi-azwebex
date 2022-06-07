# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
import pulumi_azure_native

__all__ = ['WebappArgs', 'Webapp']

@pulumi.input_type
class WebappArgs:
    def __init__(__self__, *,
                 app_sku_name: Optional[pulumi.Input[str]] = None,
                 app_sku_tier: Optional[pulumi.Input[str]] = None,
                 container_public_access: Optional[Any] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input['pulumi_azure_native.resources.ResourceGroup']] = None,
                 storage_account: Optional[pulumi.Input['pulumi_azure_native.storage.StorageAccount']] = None,
                 storage_sku_name: Optional[Any] = None):
        """
        The set of arguments for constructing a Webapp resource.
        :param pulumi.Input[str] app_sku_name: The name of the compute instance running the server. Also see appSkuTier
        :param pulumi.Input[str] app_sku_tier: The tier of the compute instance running the server. Also see appSkuName
        :param Any container_public_access: The public access level of the BlobContainer containg the website data.
        :param pulumi.Input[str] file_path: The relative file path to the folder containing web files.
        :param pulumi.Input[str] name_prefix: The name prefix given to child resources of this component. Should not contain dashes.
        :param pulumi.Input['pulumi_azure_native.resources.ResourceGroup'] resource_group: The resource group to use. One will be created if not provided.
        :param pulumi.Input['pulumi_azure_native.storage.StorageAccount'] storage_account: The storage account to use. One will be created if not provided.
        :param Any storage_sku_name: The name of the SKU of the storage account created, if storageAccount is not provided
        """
        if app_sku_name is None:
            app_sku_name = 'B1'
        if app_sku_name is not None:
            pulumi.set(__self__, "app_sku_name", app_sku_name)
        if app_sku_tier is None:
            app_sku_tier = 'Basic'
        if app_sku_tier is not None:
            pulumi.set(__self__, "app_sku_tier", app_sku_tier)
        if container_public_access is not None:
            pulumi.set(__self__, "container_public_access", container_public_access)
        if file_path is None:
            file_path = 'wwwroot'
        if file_path is not None:
            pulumi.set(__self__, "file_path", file_path)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if resource_group is not None:
            pulumi.set(__self__, "resource_group", resource_group)
        if storage_account is not None:
            pulumi.set(__self__, "storage_account", storage_account)
        if storage_sku_name is not None:
            pulumi.set(__self__, "storage_sku_name", storage_sku_name)

    @property
    @pulumi.getter(name="appSkuName")
    def app_sku_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the compute instance running the server. Also see appSkuTier
        """
        return pulumi.get(self, "app_sku_name")

    @app_sku_name.setter
    def app_sku_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_sku_name", value)

    @property
    @pulumi.getter(name="appSkuTier")
    def app_sku_tier(self) -> Optional[pulumi.Input[str]]:
        """
        The tier of the compute instance running the server. Also see appSkuName
        """
        return pulumi.get(self, "app_sku_tier")

    @app_sku_tier.setter
    def app_sku_tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_sku_tier", value)

    @property
    @pulumi.getter(name="containerPublicAccess")
    def container_public_access(self) -> Optional[Any]:
        """
        The public access level of the BlobContainer containg the website data.
        """
        return pulumi.get(self, "container_public_access")

    @container_public_access.setter
    def container_public_access(self, value: Optional[Any]):
        pulumi.set(self, "container_public_access", value)

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[str]]:
        """
        The relative file path to the folder containing web files.
        """
        return pulumi.get(self, "file_path")

    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_path", value)

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
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[pulumi.Input['pulumi_azure_native.storage.StorageAccount']]:
        """
        The storage account to use. One will be created if not provided.
        """
        return pulumi.get(self, "storage_account")

    @storage_account.setter
    def storage_account(self, value: Optional[pulumi.Input['pulumi_azure_native.storage.StorageAccount']]):
        pulumi.set(self, "storage_account", value)

    @property
    @pulumi.getter(name="storageSkuName")
    def storage_sku_name(self) -> Optional[Any]:
        """
        The name of the SKU of the storage account created, if storageAccount is not provided
        """
        return pulumi.get(self, "storage_sku_name")

    @storage_sku_name.setter
    def storage_sku_name(self, value: Optional[Any]):
        pulumi.set(self, "storage_sku_name", value)


class Webapp(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_sku_name: Optional[pulumi.Input[str]] = None,
                 app_sku_tier: Optional[pulumi.Input[str]] = None,
                 container_public_access: Optional[Any] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input['pulumi_azure_native.resources.ResourceGroup']] = None,
                 storage_account: Optional[pulumi.Input['pulumi_azure_native.storage.StorageAccount']] = None,
                 storage_sku_name: Optional[Any] = None,
                 __props__=None):
        """
        Create a Webapp resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_sku_name: The name of the compute instance running the server. Also see appSkuTier
        :param pulumi.Input[str] app_sku_tier: The tier of the compute instance running the server. Also see appSkuName
        :param Any container_public_access: The public access level of the BlobContainer containg the website data.
        :param pulumi.Input[str] file_path: The relative file path to the folder containing web files.
        :param pulumi.Input[str] name_prefix: The name prefix given to child resources of this component. Should not contain dashes.
        :param pulumi.Input['pulumi_azure_native.resources.ResourceGroup'] resource_group: The resource group to use. One will be created if not provided.
        :param pulumi.Input['pulumi_azure_native.storage.StorageAccount'] storage_account: The storage account to use. One will be created if not provided.
        :param Any storage_sku_name: The name of the SKU of the storage account created, if storageAccount is not provided
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[WebappArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Webapp resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param WebappArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebappArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_sku_name: Optional[pulumi.Input[str]] = None,
                 app_sku_tier: Optional[pulumi.Input[str]] = None,
                 container_public_access: Optional[Any] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input['pulumi_azure_native.resources.ResourceGroup']] = None,
                 storage_account: Optional[pulumi.Input['pulumi_azure_native.storage.StorageAccount']] = None,
                 storage_sku_name: Optional[Any] = None,
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
            __props__ = WebappArgs.__new__(WebappArgs)

            if app_sku_name is None:
                app_sku_name = 'B1'
            __props__.__dict__["app_sku_name"] = app_sku_name
            if app_sku_tier is None:
                app_sku_tier = 'Basic'
            __props__.__dict__["app_sku_tier"] = app_sku_tier
            __props__.__dict__["container_public_access"] = container_public_access
            if file_path is None:
                file_path = 'wwwroot'
            __props__.__dict__["file_path"] = file_path
            __props__.__dict__["name_prefix"] = name_prefix
            __props__.__dict__["resource_group"] = resource_group
            __props__.__dict__["storage_account"] = storage_account
            __props__.__dict__["storage_sku_name"] = storage_sku_name
            __props__.__dict__["url"] = None
        super(Webapp, __self__).__init__(
            'azure-justrun:index:webapp',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "url")
