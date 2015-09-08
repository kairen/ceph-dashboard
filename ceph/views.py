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
    print models.health()
    return render(
        request, 'health/health.html', {
            'current_time': datetime.now(),
            'health_alerts': models.health()
        })

# # osd 儀表板
# def cluster_osd_view(request):
#     health = models.health()
#     osd = models.osd()
#     return render(
#         request, 'osd/osd.html', {
#             'current_time': datetime.now(),
#             'pool_details': models.pools(),
#             'cluster_nodes': osd["cluster_nodes"],
#             'health_message': health["health_message"],
#             'health_detail': health["health_detail"],
#             'osd_message': health["osd_message"],
#             'mon_message': health["mon_message"],
#             'err_count': health["err_count"],
#             'warn_count': health["warn_count"]
#         }
#     )
#
# # mon 儀表板
# def cluster_mon_view(request):
#     models = ModelsData()
#     health = models.health()
#     return render(
#         request, 'mon/mon.html', {
#             'current_time': datetime.now(),
#             'pool_details': models.pools(),
#             'health_message': health["health_message"],
#             'health_detail': health["health_detail"],
#             'osd_message': health["osd_message"],
#             'mon_message': health["mon_message"],
#             'err_count': health["err_count"],
#             'warn_count': health["warn_count"]
#         }
#     )
#
# # pool 儀表板
# def cluster_pool_view(request):
#     health = models.health()
#
#     return render(
#         request, 'pool/pool.html', {
#             'current_time': datetime.now(),
#             'health_message': health["health_message"],
#             'pool_details': models.pools(),
#             'health_detail': health["health_detail"],
#             'osd_message': health["osd_message"],
#             'mon_message': health["mon_message"],
#             'err_count': health["err_count"],
#             'warn_count': health["warn_count"]
#         }
#     )
#
# # pool args
# def cluster_pool_args_view(request):
#     health = models.health()
#
#     return render(
#         request, 'pool/pool_args/pool_args.html', {
#             'current_time': datetime.now(),
#             'health_message': health["health_message"],
#             'pool_details': models.pools(),
#             'health_detail': health["health_detail"],
#             'osd_message': health["osd_message"],
#             'mon_message': health["mon_message"],
#             'err_count': health["err_count"],
#             'warn_count': health["warn_count"]
#         }
#     )
#
# # mds 儀表板
# def cluster_mds_view(request):
#     health = models.health()
#     return render(
#         request, 'mds/mds.html', {
#             'current_time': datetime.now(),
#             'pool_details': models.pools(),
#             'health_message': health["health_message"],
#             'health_detail': health["health_detail"],
#             'osd_message': health["osd_message"],
#             'mon_message': health["mon_message"],
#             'err_count': health["err_count"],
#             'warn_count': health["warn_count"]
#         }
#     )