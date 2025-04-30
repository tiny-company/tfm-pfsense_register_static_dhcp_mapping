variable "python_version" {
  type      = string
  default   = "3.11.2"
}

####################################################
#            dhcp static record vars
####################################################

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

####################################################
#             pfsense provider vars
####################################################

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











