# coding=utf-8
from datetime import datetime
from django.shortcuts import render

# health 儀表板
def cluster_health_view(request):
    return render(
        request, 'health/health.html',
        {
            'current_time': datetime.now(),
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
                    'left_value': '192',
                    'right_title': 'Clean',
                    'right_value': '192',
                    'icon': 'fa-desktop'
                },
                {
                    'tag': '1',
                    'title': 'Usage 狀態',
                    'left_title': 'Usage',
                    'left_value': '102.2 GB',
                    'right_title': 'Total',
                    'right_value': '563.3 GB',
                    'icon': ' fa-inbox'
                },
                {
                    'tag': '2',
                    'title': 'Host 狀態',
                    'left_title': 'OSD',
                    'left_value': '3',
                    'right_title': 'MON',
                    'right_value': '2',
                    'icon': 'fa-desktop'
                }
            ]
        }
    )


# osd 儀表板
def cluster_osd_view(request):
    return render(
        request, 'osd/osd.html', {'current_time': datetime.now()}
    )


# mon 儀表板
def cluster_mon_view(request):
    return render(
        request, 'mon/mon.html', {'current_time': datetime.now()}
    )

