// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package azurejustrun

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This represents a web app component resource
type Webapp struct {
	pulumi.ResourceState

	// The URL of the web app
	Url pulumi.StringPtrOutput `pulumi:"url"`
}

// NewWebapp registers a new resource with the given unique name, arguments, and options.
func NewWebapp(ctx *pulumi.Context,
	name string, args *WebappArgs, opts ...pulumi.ResourceOption) (*Webapp, error) {
	if args == nil {
		args = &WebappArgs{}
	}

	if isZero(args.FilePath) {
		args.FilePath = pulumi.StringPtr("./www")
	}
	var resource Webapp
	err := ctx.RegisterRemoteComponentResource("azure-justrun:index:webapp", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type webappArgs struct {
	// The tier of the compute instance running the server. Also see appSkuName
	AppSkuName *string `pulumi:"appSkuName"`
	// The name of the compute instance running the server. Also see appSkuTier
	AppSkuTier *string `pulumi:"appSkuTier"`
	// The public access level of the BlobContainer containg the website data.
	ContainerPublicAccess *PublicAccess `pulumi:"containerPublicAccess"`
	// The relative file path to the folder containing web files.
	FilePath *string `pulumi:"filePath"`
	// The name prefix given to child resources of this component. Should not contain dashes.
	NamePrefix *string `pulumi:"namePrefix"`
	// The resource group to use. One will be created if not provided.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// The name of the storage account to use. One will be created if not provided.
	StorageAccountName *string `pulumi:"storageAccountName"`
	// The SKU name of the storage account created, if storageAccount is not provided
	StorageSkuName *StorageSkuName `pulumi:"storageSkuName"`
}

// The set of arguments for constructing a Webapp resource.
type WebappArgs struct {
	// The tier of the compute instance running the server. Also see appSkuName
	AppSkuName pulumi.StringPtrInput
	// The name of the compute instance running the server. Also see appSkuTier
	AppSkuTier pulumi.StringPtrInput
	// The public access level of the BlobContainer containg the website data.
	ContainerPublicAccess PublicAccessPtrInput
	// The relative file path to the folder containing web files.
	FilePath pulumi.StringPtrInput
	// The name prefix given to child resources of this component. Should not contain dashes.
	NamePrefix pulumi.StringPtrInput
	// The resource group to use. One will be created if not provided.
	ResourceGroupName pulumi.StringPtrInput
	// The name of the storage account to use. One will be created if not provided.
	StorageAccountName pulumi.StringPtrInput
	// The SKU name of the storage account created, if storageAccount is not provided
	StorageSkuName StorageSkuNamePtrInput
}

func (WebappArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*webappArgs)(nil)).Elem()
}

type WebappInput interface {
	pulumi.Input

	ToWebappOutput() WebappOutput
	ToWebappOutputWithContext(ctx context.Context) WebappOutput
}

func (*Webapp) ElementType() reflect.Type {
	return reflect.TypeOf((**Webapp)(nil)).Elem()
}

func (i *Webapp) ToWebappOutput() WebappOutput {
	return i.ToWebappOutputWithContext(context.Background())
}

func (i *Webapp) ToWebappOutputWithContext(ctx context.Context) WebappOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebappOutput)
}

// WebappArrayInput is an input type that accepts WebappArray and WebappArrayOutput values.
// You can construct a concrete instance of `WebappArrayInput` via:
//
//          WebappArray{ WebappArgs{...} }
type WebappArrayInput interface {
	pulumi.Input

	ToWebappArrayOutput() WebappArrayOutput
	ToWebappArrayOutputWithContext(context.Context) WebappArrayOutput
}

type WebappArray []WebappInput

func (WebappArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Webapp)(nil)).Elem()
}

func (i WebappArray) ToWebappArrayOutput() WebappArrayOutput {
	return i.ToWebappArrayOutputWithContext(context.Background())
}

func (i WebappArray) ToWebappArrayOutputWithContext(ctx context.Context) WebappArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebappArrayOutput)
}

// WebappMapInput is an input type that accepts WebappMap and WebappMapOutput values.
// You can construct a concrete instance of `WebappMapInput` via:
//
//          WebappMap{ "key": WebappArgs{...} }
type WebappMapInput interface {
	pulumi.Input

	ToWebappMapOutput() WebappMapOutput
	ToWebappMapOutputWithContext(context.Context) WebappMapOutput
}

type WebappMap map[string]WebappInput

func (WebappMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Webapp)(nil)).Elem()
}

func (i WebappMap) ToWebappMapOutput() WebappMapOutput {
	return i.ToWebappMapOutputWithContext(context.Background())
}

func (i WebappMap) ToWebappMapOutputWithContext(ctx context.Context) WebappMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebappMapOutput)
}

type WebappOutput struct{ *pulumi.OutputState }

func (WebappOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Webapp)(nil)).Elem()
}

func (o WebappOutput) ToWebappOutput() WebappOutput {
	return o
}

func (o WebappOutput) ToWebappOutputWithContext(ctx context.Context) WebappOutput {
	return o
}

// The URL of the web app
func (o WebappOutput) Url() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Webapp) pulumi.StringPtrOutput { return v.Url }).(pulumi.StringPtrOutput)
}

type WebappArrayOutput struct{ *pulumi.OutputState }

func (WebappArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Webapp)(nil)).Elem()
}

func (o WebappArrayOutput) ToWebappArrayOutput() WebappArrayOutput {
	return o
}

func (o WebappArrayOutput) ToWebappArrayOutputWithContext(ctx context.Context) WebappArrayOutput {
	return o
}

func (o WebappArrayOutput) Index(i pulumi.IntInput) WebappOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Webapp {
		return vs[0].([]*Webapp)[vs[1].(int)]
	}).(WebappOutput)
}

type WebappMapOutput struct{ *pulumi.OutputState }

func (WebappMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Webapp)(nil)).Elem()
}

func (o WebappMapOutput) ToWebappMapOutput() WebappMapOutput {
	return o
}

func (o WebappMapOutput) ToWebappMapOutputWithContext(ctx context.Context) WebappMapOutput {
	return o
}

func (o WebappMapOutput) MapIndex(k pulumi.StringInput) WebappOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Webapp {
		return vs[0].(map[string]*Webapp)[vs[1].(string)]
	}).(WebappOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WebappInput)(nil)).Elem(), &Webapp{})
	pulumi.RegisterInputType(reflect.TypeOf((*WebappArrayInput)(nil)).Elem(), WebappArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*WebappMapInput)(nil)).Elem(), WebappMap{})
	pulumi.RegisterOutputType(WebappOutput{})
	pulumi.RegisterOutputType(WebappArrayOutput{})
	pulumi.RegisterOutputType(WebappMapOutput{})
}
