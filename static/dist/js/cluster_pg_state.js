$(function () {
        var donut = new Morris.Donut({
          element: 'pg_state',
          resize: true,
          colors: ["#cd2626", "#eba709", "#00a65a"],
          data: [
            {label: "Dirty", value: 4},
            {label: "Working", value: 3},
            {label: "Clean", value: 761}
          ],
          hideHover: 'auto'
        });
});