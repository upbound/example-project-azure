# generated by datamodel-codegen:
#   filename:  workdir/storage_azure_upbound_io_v1beta1_blobinventorypolicy.yaml

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import AwareDatetime, BaseModel, Field

from .....k8s.apimachinery.pkg.apis.meta import v1


class DeletionPolicy(Enum):
    Orphan = 'Orphan'
    Delete = 'Delete'


class FilterItem(BaseModel):
    blobTypes: Optional[List[str]] = None
    """
    A set of blob types. Possible values are blockBlob, appendBlob, and pageBlob. The storage account with is_hns_enabled is true doesn't support pageBlob.
    """
    excludePrefixes: Optional[List[str]] = None
    """
    A set of strings for blob prefixes to be excluded. Maximum of 10 blob prefixes.
    """
    includeBlobVersions: Optional[bool] = None
    """
    Includes blob versions in blob inventory or not? Defaults to false.
    """
    includeDeleted: Optional[bool] = None
    """
    Includes deleted blobs in blob inventory or not? Defaults to false.
    """
    includeSnapshots: Optional[bool] = None
    """
    Includes blob snapshots in blob inventory or not? Defaults to false.
    """
    prefixMatch: Optional[List[str]] = None
    """
    A set of strings for blob prefixes to be matched. Maximum of 10 blob prefixes.
    """


class Resolution(Enum):
    Required = 'Required'
    Optional = 'Optional'


class Resolve(Enum):
    Always = 'Always'
    IfNotPresent = 'IfNotPresent'


class Policy(BaseModel):
    resolution: Optional[Resolution] = 'Required'
    """
    Resolution specifies whether resolution of this reference is required.
    The default is 'Required', which means the reconcile will fail if the
    reference cannot be resolved. 'Optional' means this reference will be
    a no-op if it cannot be resolved.
    """
    resolve: Optional[Resolve] = None
    """
    Resolve specifies when this reference should be resolved. The default
    is 'IfNotPresent', which will attempt to resolve the reference only when
    the corresponding field is not present. Use 'Always' to resolve the
    reference on every reconcile.
    """


class StorageContainerNameRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class StorageContainerNameSelector(BaseModel):
    matchControllerRef: Optional[bool] = None
    """
    MatchControllerRef ensures an object with the same controller reference
    as the selecting object is selected.
    """
    matchLabels: Optional[Dict[str, str]] = None
    """
    MatchLabels ensures an object with matching labels is selected.
    """
    policy: Optional[Policy] = None
    """
    Policies for selection.
    """


class Rule(BaseModel):
    filter: Optional[List[FilterItem]] = None
    """
    A filter block as defined above. Can only be set when the scope is Blob.
    """
    format: Optional[str] = None
    """
    The format of the inventory files. Possible values are Csv and Parquet.
    """
    name: Optional[str] = None
    """
    The name which should be used for this Blob Inventory Policy Rule.
    """
    schedule: Optional[str] = None
    """
    The inventory schedule applied by this rule. Possible values are Daily and Weekly.
    """
    schemaFields: Optional[List[str]] = None
    """
    A list of fields to be included in the inventory. See the Azure API reference for all the supported fields.
    """
    scope: Optional[str] = None
    """
    The scope of the inventory for this rule. Possible values are Blob and Container.
    """
    storageContainerName: Optional[str] = None
    """
    The storage container name to store the blob inventory files for this rule.
    """
    storageContainerNameRef: Optional[StorageContainerNameRef] = None
    """
    Reference to a Container in storage to populate storageContainerName.
    """
    storageContainerNameSelector: Optional[StorageContainerNameSelector] = None
    """
    Selector for a Container in storage to populate storageContainerName.
    """


class StorageAccountIdRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class StorageAccountIdSelector(BaseModel):
    matchControllerRef: Optional[bool] = None
    """
    MatchControllerRef ensures an object with the same controller reference
    as the selecting object is selected.
    """
    matchLabels: Optional[Dict[str, str]] = None
    """
    MatchLabels ensures an object with matching labels is selected.
    """
    policy: Optional[Policy] = None
    """
    Policies for selection.
    """


class ForProvider(BaseModel):
    rules: Optional[List[Rule]] = None
    """
    One or more rules blocks as defined below.
    """
    storageAccountId: Optional[str] = None
    """
    The ID of the storage account to apply this Blob Inventory Policy to. Changing this forces a new Storage Blob Inventory Policy to be created.
    """
    storageAccountIdRef: Optional[StorageAccountIdRef] = None
    """
    Reference to a Account in storage to populate storageAccountId.
    """
    storageAccountIdSelector: Optional[StorageAccountIdSelector] = None
    """
    Selector for a Account in storage to populate storageAccountId.
    """


class InitProvider(BaseModel):
    rules: Optional[List[Rule]] = None
    """
    One or more rules blocks as defined below.
    """
    storageAccountId: Optional[str] = None
    """
    The ID of the storage account to apply this Blob Inventory Policy to. Changing this forces a new Storage Blob Inventory Policy to be created.
    """
    storageAccountIdRef: Optional[StorageAccountIdRef] = None
    """
    Reference to a Account in storage to populate storageAccountId.
    """
    storageAccountIdSelector: Optional[StorageAccountIdSelector] = None
    """
    Selector for a Account in storage to populate storageAccountId.
    """


class ManagementPolicy(Enum):
    Observe = 'Observe'
    Create = 'Create'
    Update = 'Update'
    Delete = 'Delete'
    LateInitialize = 'LateInitialize'
    field_ = '*'


class ProviderConfigRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class ConfigRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class Metadata(BaseModel):
    annotations: Optional[Dict[str, str]] = None
    """
    Annotations are the annotations to be added to connection secret.
    - For Kubernetes secrets, this will be used as "metadata.annotations".
    - It is up to Secret Store implementation for others store types.
    """
    labels: Optional[Dict[str, str]] = None
    """
    Labels are the labels/tags to be added to connection secret.
    - For Kubernetes secrets, this will be used as "metadata.labels".
    - It is up to Secret Store implementation for others store types.
    """
    type: Optional[str] = None
    """
    Type is the SecretType for the connection secret.
    - Only valid for Kubernetes Secret Stores.
    """


class PublishConnectionDetailsTo(BaseModel):
    configRef: Optional[ConfigRef] = Field(
        default_factory=lambda: ConfigRef.model_validate({'name': 'default'})
    )
    """
    SecretStoreConfigRef specifies which secret store config should be used
    for this ConnectionSecret.
    """
    metadata: Optional[Metadata] = None
    """
    Metadata is the metadata for connection secret.
    """
    name: str
    """
    Name is the name of the connection secret.
    """


class WriteConnectionSecretToRef(BaseModel):
    name: str
    """
    Name of the secret.
    """
    namespace: str
    """
    Namespace of the secret.
    """


class Spec(BaseModel):
    deletionPolicy: Optional[DeletionPolicy] = 'Delete'
    """
    DeletionPolicy specifies what will happen to the underlying external
    when this managed resource is deleted - either "Delete" or "Orphan" the
    external resource.
    This field is planned to be deprecated in favor of the ManagementPolicies
    field in a future release. Currently, both could be set independently and
    non-default values would be honored if the feature flag is enabled.
    See the design doc for more information: https://github.com/crossplane/crossplane/blob/499895a25d1a1a0ba1604944ef98ac7a1a71f197/design/design-doc-observe-only-resources.md?plain=1#L223
    """
    forProvider: ForProvider
    initProvider: Optional[InitProvider] = None
    """
    THIS IS A BETA FIELD. It will be honored
    unless the Management Policies feature flag is disabled.
    InitProvider holds the same fields as ForProvider, with the exception
    of Identifier and other resource reference fields. The fields that are
    in InitProvider are merged into ForProvider when the resource is created.
    The same fields are also added to the terraform ignore_changes hook, to
    avoid updating them after creation. This is useful for fields that are
    required on creation, but we do not desire to update them after creation,
    for example because of an external controller is managing them, like an
    autoscaler.
    """
    managementPolicies: Optional[List[ManagementPolicy]] = ['*']
    """
    THIS IS A BETA FIELD. It is on by default but can be opted out
    through a Crossplane feature flag.
    ManagementPolicies specify the array of actions Crossplane is allowed to
    take on the managed and external resources.
    This field is planned to replace the DeletionPolicy field in a future
    release. Currently, both could be set independently and non-default
    values would be honored if the feature flag is enabled. If both are
    custom, the DeletionPolicy field will be ignored.
    See the design doc for more information: https://github.com/crossplane/crossplane/blob/499895a25d1a1a0ba1604944ef98ac7a1a71f197/design/design-doc-observe-only-resources.md?plain=1#L223
    and this one: https://github.com/crossplane/crossplane/blob/444267e84783136daa93568b364a5f01228cacbe/design/one-pager-ignore-changes.md
    """
    providerConfigRef: Optional[ProviderConfigRef] = Field(
        default_factory=lambda: ProviderConfigRef.model_validate({'name': 'default'})
    )
    """
    ProviderConfigReference specifies how the provider that will be used to
    create, observe, update, and delete this managed resource should be
    configured.
    """
    publishConnectionDetailsTo: Optional[PublishConnectionDetailsTo] = None
    """
    PublishConnectionDetailsTo specifies the connection secret config which
    contains a name, metadata and a reference to secret store config to
    which any connection details for this managed resource should be written.
    Connection details frequently include the endpoint, username,
    and password required to connect to the managed resource.
    """
    writeConnectionSecretToRef: Optional[WriteConnectionSecretToRef] = None
    """
    WriteConnectionSecretToReference specifies the namespace and name of a
    Secret to which any connection details for this managed resource should
    be written. Connection details frequently include the endpoint, username,
    and password required to connect to the managed resource.
    This field is planned to be replaced in a future release in favor of
    PublishConnectionDetailsTo. Currently, both could be set independently
    and connection details would be published to both without affecting
    each other.
    """


class RuleModel(BaseModel):
    filter: Optional[List[FilterItem]] = None
    """
    A filter block as defined above. Can only be set when the scope is Blob.
    """
    format: Optional[str] = None
    """
    The format of the inventory files. Possible values are Csv and Parquet.
    """
    name: Optional[str] = None
    """
    The name which should be used for this Blob Inventory Policy Rule.
    """
    schedule: Optional[str] = None
    """
    The inventory schedule applied by this rule. Possible values are Daily and Weekly.
    """
    schemaFields: Optional[List[str]] = None
    """
    A list of fields to be included in the inventory. See the Azure API reference for all the supported fields.
    """
    scope: Optional[str] = None
    """
    The scope of the inventory for this rule. Possible values are Blob and Container.
    """
    storageContainerName: Optional[str] = None
    """
    The storage container name to store the blob inventory files for this rule.
    """


class AtProvider(BaseModel):
    id: Optional[str] = None
    """
    The ID of the Storage Blob Inventory Policy.
    """
    rules: Optional[List[RuleModel]] = None
    """
    One or more rules blocks as defined below.
    """
    storageAccountId: Optional[str] = None
    """
    The ID of the storage account to apply this Blob Inventory Policy to. Changing this forces a new Storage Blob Inventory Policy to be created.
    """


class Condition(BaseModel):
    lastTransitionTime: AwareDatetime
    """
    LastTransitionTime is the last time this condition transitioned from one
    status to another.
    """
    message: Optional[str] = None
    """
    A Message containing details about this condition's last transition from
    one status to another, if any.
    """
    observedGeneration: Optional[int] = None
    """
    ObservedGeneration represents the .metadata.generation that the condition was set based upon.
    For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
    with respect to the current state of the instance.
    """
    reason: str
    """
    A Reason for this condition's last transition from one status to another.
    """
    status: str
    """
    Status of this condition; is it currently True, False, or Unknown?
    """
    type: str
    """
    Type of this condition. At most one of each condition type may apply to
    a resource at any point in time.
    """


class Status(BaseModel):
    atProvider: Optional[AtProvider] = None
    conditions: Optional[List[Condition]] = None
    """
    Conditions of the resource.
    """
    observedGeneration: Optional[int] = None
    """
    ObservedGeneration is the latest metadata.generation
    which resulted in either a ready state, or stalled due to error
    it can not recover from without human intervention.
    """


class BlobInventoryPolicy(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Spec
    """
    BlobInventoryPolicySpec defines the desired state of BlobInventoryPolicy
    """
    status: Optional[Status] = None
    """
    BlobInventoryPolicyStatus defines the observed state of BlobInventoryPolicy.
    """


class BlobInventoryPolicyList(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    items: List[BlobInventoryPolicy]
    """
    List of blobinventorypolicies. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ListMeta] = None
    """
    Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """