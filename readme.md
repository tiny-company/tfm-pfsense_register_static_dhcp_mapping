# tfm-pfsense_register_static_dhcp_mapping

## Description

A simple terraform module that get create a new record in dhcp static mapping on a pfsense server.

## Usage

- Import the module by referencing it in your main terraform file (`main.tf`) using :
```hcl
module "pve_highest_lxc_id" {
  source     = "git::https://github.com/tiny-company/tfm-pve_highest_lxc_id.git"
  pfsense_url = var.pfsense_url
  pfsense_username = var.pfsense_username
  pfsense_password = var.pfsense_password
  record_data_mac = var.record_data_mac
  record_data_ip_address = var.record_data_ip_address
  record_data_cid = var.record_data_cid
  record_data_hostname = var.record_data_hostname
  record_data_domain = var.record_data_domain
}
```

- Don't forget to define the vars below in your main variables.tf :
```hcl
variable "python_version" {
  type      = string
  default   = "3.11.2"
}

variable "record_data_mac" {
  type      = string
  sensitive = true
}

variable "record_data_ip_address" {
  type      = string
  sensitive = true
}

variable "record_data_cid" {
  type      = string
  sensitive = true
}

variable "record_data_hostname" {
  type      = string
  sensitive = true
}

variable "record_data_domain" {
  type      = string
  sensitive = true
}

variable "pfsense_url" {
  type      = string
  sensitive = true
}


variable "pfsense_username" {
  type      = string
  sensitive = true
}


variable "pfsense_password" {
  type      = string
  sensitive = true
}

```

- And finally don't forget to set **these vars** and **the vars for the proxmox/bpg provider** in a .tfvars (i.e: `terraform.tfvars`) file  :
```hcl
pfsense_url="192.168.0.1"
pfsense_username="pfsense_username"
pfsense_password="pfsense_api_token"
record_data_mac="xx:xx:xx:xx:xx:xx"
record_data_ip_address="192.168.0.150"
record_data_cid="192.168.0.150"
record_data_hostname="test"
record_data_domain="domain.com"
```

## Sources :

- [tutorial terraform module](https://developer.hashicorp.com/terraform/tutorials/modules/module)
- [terraform module creation guide](https://developer.hashicorp.com/terraform/language/modules/develop)
- [terraform module source](https://developer.hashicorp.com/terraform/language/modules/sources#github)
- [terraform module git private repo source](https://medium.com/@dipandergoyal/terraform-using-private-git-repo-as-module-source-d20d8cec7c5)