resource "huaweicloud_vpc_v1" "test" {
  name = "cce-test"
  cidr = "192.168.0.0/16"
}

resource "huaweicloud_vpc_subnet_v1" "test" {
  name          = "cce-test"
  cidr          = "192.168.0.0/16"
  gateway_ip    = "192.168.0.1"

  //dns is required for cce node installing
  primary_dns   = "100.125.1.250"
  secondary_dns = "100.125.21.250"
  vpc_id        = huaweicloud_vpc_v1.test.id
}


data "huaweicloud_availability_zones" "myaz" {}

resource "huaweicloud_vpc_eip" "myeip" {
  publicip {
    type = "5_bgp"
  }
  bandwidth {
    name        = "cce-test"
    size        = 8
    share_type  = "PER"
    charge_mode = "traffic"
  }
}

resource "huaweicloud_compute_keypair" "test-keypair" {
  name       = "keypair"
}
resource "huaweicloud_cce_cluster" "test" {
  name                   = "cce-test"
  flavor_id              = "cce.s1.small"
  vpc_id                 = huaweicloud_vpc_v1.test.id
  subnet_id              = huaweicloud_vpc_subnet_v1.test.id
  container_network_type = "overlay_l2"
  eip                    = huaweicloud_vpc_eip.myeip.address
}

resource "huaweicloud_cce_node" "node" {
  cluster_id        = huaweicloud_cce_cluster.test.id
  name              = "node"
  flavor_id         = "t6.large.2"
  availability_zone = data.huaweicloud_availability_zones.myaz.names[0]
  key_pair          = huaweicloud_compute_keypair.test-keypair.name

  root_volume {
    size       = 40
    volumetype = "SAS"
  }
  data_volumes {
    size       = 100
    volumetype = "SAS"
  }
}


data "huaweicloud_cce_cluster" "cluster_by_id" {
	id = huaweicloud_cce_cluster.test.id
}

output "found_cluster" {
    value = "${data.huaweicloud_cce_cluster.cluster_by_id.kube_config_raw}"
}