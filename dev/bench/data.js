window.BENCHMARK_DATA = {
  "lastUpdate": 1720003669466,
  "repoUrl": "https://github.com/GiadaLalli/ISN-tractor",
  "entries": {
    "ISN-Tractor Performance Regression Tests": [
      {
        "commit": {
          "author": {
            "email": "james.collier@vib.be",
            "name": "James Collier",
            "username": "MaybeJustJames"
          },
          "committer": {
            "email": "james.collier@vib.be",
            "name": "James Collier",
            "username": "MaybeJustJames"
          },
          "distinct": true,
          "id": "9fa30a6fa0897913aa679ed6c5fe13347ca39fe8",
          "message": "Fix typo: branch name in benchmark action",
          "timestamp": "2024-07-03T10:20:16+02:00",
          "tree_id": "1c90aa8c27e22d15eaf062b74a3e5dd482e63d08",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/9fa30a6fa0897913aa679ed6c5fe13347ca39fe8"
        },
        "date": 1719995035945,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_sparse_200_500_cpu",
            "value": 9.761383356556399,
            "unit": "iter/sec",
            "range": "stddev: 0.03923988651684272",
            "extra": "mean: 102.44449618181761 msec\nrounds: 11"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "26444312+MaybeJustJames@users.noreply.github.com",
            "name": "James Collier",
            "username": "MaybeJustJames"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "037b40fca5898fe1e72550dfbff64314669902f9",
          "message": "Biweight midcorrelation metric (#45)\n\n* Add a new metric: biweight_midcorrelation, selected with a `metric=\"biweight\"` argument.\r\n* Improve overall sparse_isn performance\r\n* Output a diff in CI when formatting check fails\r\n* Add performance regression benchmarks and publish results to GHPages\r\n* Allow importing the benchmark module without needing pyperf\r\n* Update dependencies",
          "timestamp": "2024-07-03T20:40:11+10:00",
          "tree_id": "fe25cb6bfe984eee04cce041b6fe4272c2794269",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/037b40fca5898fe1e72550dfbff64314669902f9"
        },
        "date": 1720003669175,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 4.393226393331528,
            "unit": "iter/sec",
            "range": "stddev: 0.004418668595763448",
            "extra": "mean: 227.62314310000022 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 4.20138945101727,
            "unit": "iter/sec",
            "range": "stddev: 0.0027047264281485923",
            "extra": "mean: 238.01649708000127 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 3.338919716750856,
            "unit": "iter/sec",
            "range": "stddev: 0.006332069546209397",
            "extra": "mean: 299.49806668999884 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 4.323765338966582,
            "unit": "iter/sec",
            "range": "stddev: 0.006613121351422823",
            "extra": "mean: 231.27989647999925 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 4.127114417326587,
            "unit": "iter/sec",
            "range": "stddev: 0.006609806704488093",
            "extra": "mean: 242.30004280999992 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 4.536818089234067,
            "unit": "iter/sec",
            "range": "stddev: 0.004476792928489834",
            "extra": "mean: 220.41880021000054 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 2.1454880630266198,
            "unit": "iter/sec",
            "range": "stddev: 0.006889542631884683",
            "extra": "mean: 466.09441330999965 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 2.069177938891619,
            "unit": "iter/sec",
            "range": "stddev: 0.007531704574690288",
            "extra": "mean: 483.28371436999873 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 2.1544928697939136,
            "unit": "iter/sec",
            "range": "stddev: 0.007481205082755242",
            "extra": "mean: 464.14634924999973 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 7.919952053021951,
            "unit": "iter/sec",
            "range": "stddev: 0.006420012830145444",
            "extra": "mean: 126.26339065000252 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 7.003241421788938,
            "unit": "iter/sec",
            "range": "stddev: 0.006602040105543409",
            "extra": "mean: 142.79102200999887 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 8.302817812667318,
            "unit": "iter/sec",
            "range": "stddev: 0.006882387217356924",
            "extra": "mean: 120.44103851999921 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 184.17386737978973,
            "unit": "iter/sec",
            "range": "stddev: 0.00028692731512896315",
            "extra": "mean: 5.429651960002957 msec\nrounds: 20"
          }
        ]
      }
    ]
  }
}