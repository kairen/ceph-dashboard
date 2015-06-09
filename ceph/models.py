from django.db import models

# Create your models here.

from cephclient.wrapper import *

class ModelsData:

    def __init__(self):
        self.rest_client = CephWrapper(
            endpoint='http://163.17.136.249:5100/api/v1/',
            debug=False
        )

    def health(self):
        response, body = self.rest_client.status(body='json')
        health = body["output"]["health"]
        osd_map = body["output"]["osdmap"]["osdmap"]
        pg_map = body["output"]["pgmap"]
        mom_quorum_count = 0
        mon_map_count = 0
        mon_msg_count = 0
        warn_count = 0
        err_count = 0

        # for mon_msg in body["output"]["health"]["timechecks"]["mons"]:
        #     if mon_msg["health"] == "HEALTH_WARN" or mon_msg["health"] == "HEALTH_ERR":
        #         mon_msg_count += 1

        for quorum in body["output"]["quorum"]:
             mom_quorum_count += 1

        for mon in body["output"]["monmap"]["mons"]:
             mon_map_count += 1

        for detail in body["output"]["health"]["summary"]:
            if detail["severity"] == 'HEALTH_WARN':
                warn_count += 1
            elif detail["severity"] == 'HEALTH_ERR':
                err_count += 1

        response, body = self.rest_client.osd_lspools(body='json')
        pools_map_count = 0

        for pool in body["output"]:
            pools_map_count += 1

        osd_warn_count = osd_map["num_osds"] - osd_map["num_in_osds"];

        return {
            'health_message': health["overall_status"],
            'health_detail': health["summary"],
            'warn_count': warn_count,
            'err_count': err_count,
            'osd_message': {
                'osd_total': osd_map["num_osds"],
                'osd_in': osd_map["num_in_osds"],
                'osd_up': osd_map["num_up_osds"],
                'osd_counter': osd_warn_count
            },
            'mon_message': {
                'quorum_count': 1,
                'mon_count': 1,
                'msg_count': 0
            },
            'pool_message': pools_map_count,
        }

    def osd(self):
        response, body = self.rest_client.osd_dump(body='json')

        return {
            'cluster_nodes': body['output']['osds'],
        }

    def pools(self):

        response, osd_pools = self.rest_client.osd_pool_ls('',body='json')

        pools = []
        for pg_pool in osd_pools["output"]:
            pools.append({
                'size': pg_pool["size"],
                'pg_placement_num': pg_pool["pg_placement_num"]
            })

        pool_dirty = 0
        count = 0
        response, df_pools = self.rest_client.df('', body='json')
        for df_pool in df_pools["output"]["pools"]:
            pools[count].update({
                'id': df_pool["id"],
                'name': df_pool["name"]
            })
            for key in df_pool["stats"].keys():
                if key == 'dirty':
                    pool_dirty += df_pool["stats"][key]

                pools[count].update({
                    key: df_pool["stats"][key]
            })
            count += 1

        return {
            'pools': pools,
            'pool_message': pool_dirty
        }