
# ------------------------------------------------------------------
# - Filename: main.tf
# - Author : draed
# - Dependency : none
# - Description : terraform module that set a dhcp static mapping on a pfsense server
# - Creation date : 2025-04-30
# - terraform version : OpenTofu v1.9.0
# ------------------------------------------------------------------

resource "null_resource" "set_static_dhcp_mapping" {
  provisioner "local-exec" {
    command = "virtualenv -p ${var.python_version} ${path.module}/venv && ${path.module}/venv/bin/python -m pip install -r ${path.module}/scripts/requirements.txt && ${path.module}/venv/bin/python ${path.module}/scripts/set_static_dhcp_mapping.py"
    environment = {
      RECORD_DATA_MAC = "${var.record_data_mac}"
      RECORD_DATA_IP_ADDRESS = "${var.record_data_ip_address}"
      RECORD_DATA_CID = "${var.record_data_cid}"
      RECORD_DATA_HOSTNAME = "${var.record_data_hostname}"
      RECORD_DATA_DOMAIN = "${var.record_data_domain}"
      PFSENSE_URL = "${var.pfsense_url}"
      PFSENSE_USERNAME = "${var.pfsense_username}"
      PFSENSE_PASSWORD = "${var.pfsense_password}"
    }
  }
}

resource "null_resource" "delete_static_dhcp_mapping" {
  triggers = {
      record_data_mac = var.record_data_mac
      record_data_ip_address = var.record_data_ip_address
      record_data_cid = var.record_data_cid
      record_data_hostname = var.record_data_hostname
      record_data_domain = var.record_data_domain
      pfsense_url = var.pfsense_url
      pfsense_username = var.pfsense_username
      pfsense_password = var.pfsense_password
    }
  provisioner "local-exec" {
    when    = destroy
    command = "virtualenv -p ${var.python_version} ${path.module}/venv && ${path.module}/venv/bin/python -m pip install -r ${path.module}/scripts/requirements.txt && ${path.module}/venv/bin/python ${path.module}/scripts/delete_static_dhcp_mapping.py"
    environment = {
      RECORD_DATA_MAC = "${self.triggers.record_data_mac}"
      RECORD_DATA_IP_ADDRESS = "${self.triggers.record_data_ip_address}"
      RECORD_DATA_CID = "${self.triggers.record_data_cid}"
      RECORD_DATA_HOSTNAME = "${self.triggers.record_data_hostname}"
      RECORD_DATA_DOMAIN = "${self.triggers.record_data_domain}"
      PFSENSE_URL = "${self.triggers.pfsense_url}"
      PFSENSE_USERNAME = "${self.triggers.pfsense_username}"
      PFSENSE_PASSWORD = "${self.triggers.pfsense_password}"
    }
  }
}