
# ------------------------------------------------------------------
# - Filename: main.tf
# - Author : draed
# - Dependency : none
# - Description : terraform module that set a dhcp static mapping on a pfsense server
# - Creation date : 2025-04-30
# - terraform version : OpenTofu v1.9.0
# ------------------------------------------------------------------

resource "null_resource" "import_script_dependencies" {
  provisioner "local-exec" {
    command = "virtualenv -p ${var.python_version} ${path.module}/venv && ${path.module}/venv/bin/python -m pip install -r ${path.module}/scripts/requirements.txt"
  }
}

resource "null_resource" "set_static_dhcp_mapping" {
  depends_on = [null_resource.import_script_dependencies]
  provisioner "local-exec" {
    command = "${path.module}/venv/bin/python ${path.module}/scripts/set_static_dhcp_mapping.py"
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

