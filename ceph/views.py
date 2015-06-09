# coding=utf-8
from datetime import datetime
from django.shortcuts import render
from ceph.models import ModelsData


models = ModelsData()



# login 儀表板
def dashboard_login_view(request):
    return render(request, 'base/login.html', {'current_time': datetime.now()})


# health 儀表板
def cluster_health_view(request):
    health = models.health()
    return render(
        request, 'health/health.html',
        {
            'current_time': datetime.now(),
            'err_count': health["err_count"],
            'pool_details': models.pools(),
            'warn_count': health["warn_count"],
            'health_message': health["health_message"],
            'health_detail': health["health_detail"],
            'osd_message': health["osd_message"],
            'mon_message': health["mon_message"],
            'pool_message': health["pool_message"],
            'performance_row': [
                {
                    'id': 'writes_iops',
                    'title': '叢集寫入 IOPS 狀態',
                },
                {
                    'id': 'reads_iops',
                    'title': '叢集讀取 IOPS 狀態',
                },
                {
                    'id': 'cluster_ops',
                    'title': ' 叢集 OPS 狀態',
                },
            ],
            'row_three_content': [
                {
                    'tag': '0',
                    'title': 'Placement Groups 狀態',
                    'left_title': 'Active',
                    'left_value': '896',
                    'right_title': 'Clean',
                    'right_value': '889',
                    'icon': 'fa-sitemap'
                },
                {
                    'tag': '1',
                    'title': 'Usage 狀態',
                    'left_title': 'Usage',
                    'left_value': 102.2,
                    'right_title': 'Total',
                    'right_value': 1157,
                    'total_value': round((102.2 / 1157) * 100, 2),
                    'icon': ' fa-inbox'
                },
                {
                    'tag': '2',
                    'title': 'Host 狀態',
                    'left_title': 'OSD',
                    'left_value': '8',
                    'right_title': 'MON',
                    'right_value': '2',
                    'icon': 'fa-desktop'
                }
            ]
        }
    )

# osd 儀表板
def cluster_osd_view(request):
    health = models.health()
    osd = models.osd()
    return render(
        request, 'osd/osd.html', {
            'current_time': datetime.now(),
            'pool_details': models.pools(),
            'cluster_nodes': osd["cluster_nodes"],
            'health_message': health["health_message"],
            'health_detail': health["health_detail"],
            'osd_message': health["osd_message"],
            'mon_message': health["mon_message"],
            'err_count': health["err_count"],
            'warn_count': health["warn_count"]
        }
    )

# mon 儀表板
def cluster_mon_view(request):
    models = ModelsData()
    health = models.health()
    return render(
        request, 'mon/mon.html', {
            'current_time': datetime.now(),
            'pool_details': models.pools(),
            'health_message': health["health_message"],
            'health_detail': health["health_detail"],
            'osd_message': health["osd_message"],
            'mon_message': health["mon_message"],
            'err_count': health["err_count"],
            'warn_count': health["warn_count"]
        }
    )

# pool 儀表板
def cluster_pool_view(request):
    health = models.health()

    return render(
        request, 'pool/pool.html', {
            'current_time': datetime.now(),
            'health_message': health["health_message"],
            'pool_details': models.pools(),
            'health_detail': health["health_detail"],
            'osd_message': health["osd_message"],
            'mon_message': health["mon_message"],
            'err_count': health["err_count"],
            'warn_count': health["warn_count"]
        }
    )

# pool args
def cluster_pool_args_view(request):
    health = models.health()

    return render(
        request, 'pool/pool_args/pool_args.html', {
            'current_time': datetime.now(),
            'health_message': health["health_message"],
            'pool_details': models.pools(),
            'health_detail': health["health_detail"],
            'osd_message': health["osd_message"],
            'mon_message': health["mon_message"],
            'err_count': health["err_count"],
            'warn_count': health["warn_count"]
        }
    )

# mds 儀表板
def cluster_mds_view(request):
    health = models.health()
    return render(
        request, 'mds/mds.html', {
            'current_time': datetime.now(),
            'pool_details': models.pools(),
            'health_message': health["health_message"],
            'health_detail': health["health_detail"],
            'osd_message': health["osd_message"],
            'mon_message': health["mon_message"],
            'err_count': health["err_count"],
            'warn_count': health["warn_count"]
        }
    )