window.BENCHMARK_DATA = {
  "lastUpdate": 1720014841962,
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
      },
      {
        "commit": {
          "author": {
            "email": "45395344+GiadaLalli@users.noreply.github.com",
            "name": "Giada Lalli",
            "username": "GiadaLalli"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "7396aae60c352a32831be38210f4c2022c525704",
          "message": "Update test_benchmark.py",
          "timestamp": "2024-07-03T15:03:24+02:00",
          "tree_id": "587d6e1335b74119917eda6cce98356bb41e6dad",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/7396aae60c352a32831be38210f4c2022c525704"
        },
        "date": 1720012302988,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 3.819690394826236,
            "unit": "iter/sec",
            "range": "stddev: 0.007719676694786033",
            "extra": "mean: 261.8013233099987 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 3.682715682248524,
            "unit": "iter/sec",
            "range": "stddev: 0.006661025822330924",
            "extra": "mean: 271.5387464799994 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 2.90129266283391,
            "unit": "iter/sec",
            "range": "stddev: 0.01095701492511262",
            "extra": "mean: 344.6739492400002 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 3.7450767124166546,
            "unit": "iter/sec",
            "range": "stddev: 0.010181271580967625",
            "extra": "mean: 267.0172273600002 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 3.560223940179243,
            "unit": "iter/sec",
            "range": "stddev: 0.007978098472022317",
            "extra": "mean: 280.88120770000046 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 3.787115841976578,
            "unit": "iter/sec",
            "range": "stddev: 0.008533196289151617",
            "extra": "mean: 264.05318498999975 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.8577263996840268,
            "unit": "iter/sec",
            "range": "stddev: 0.011572399497934234",
            "extra": "mean: 538.2923987999988 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.7883281640879818,
            "unit": "iter/sec",
            "range": "stddev: 0.009099928113447089",
            "extra": "mean: 559.181485859998 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.8651347197177237,
            "unit": "iter/sec",
            "range": "stddev: 0.0108709487577585",
            "extra": "mean: 536.1542999700008 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 6.707425077438191,
            "unit": "iter/sec",
            "range": "stddev: 0.008699993400617115",
            "extra": "mean: 149.08850839999786 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 5.9614291986183705,
            "unit": "iter/sec",
            "range": "stddev: 0.007539461241186057",
            "extra": "mean: 167.74500990999968 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 7.1650701541419375,
            "unit": "iter/sec",
            "range": "stddev: 0.007704052858527071",
            "extra": "mean: 139.56597471999999 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 179.7773264012365,
            "unit": "iter/sec",
            "range": "stddev: 0.00030883554857554424",
            "extra": "mean: 5.562436710000611 msec\nrounds: 20"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "45395344+GiadaLalli@users.noreply.github.com",
            "name": "Giada Lalli",
            "username": "GiadaLalli"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "34f868df71e63574060b4d6fb7b13ccc6f241962",
          "message": "Update dense_isn_offline.py",
          "timestamp": "2024-07-03T15:01:55+02:00",
          "tree_id": "a282d8f1f88b62091ffaac04b7d3825c4f323c68",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/34f868df71e63574060b4d6fb7b13ccc6f241962"
        },
        "date": 1720012634182,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 3.957638322425007,
            "unit": "iter/sec",
            "range": "stddev: 0.005460325613886096",
            "extra": "mean: 252.67594422000116 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 3.758674961343103,
            "unit": "iter/sec",
            "range": "stddev: 0.004219428490296368",
            "extra": "mean: 266.05120428999953 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 2.9395570542551424,
            "unit": "iter/sec",
            "range": "stddev: 0.014834080048365249",
            "extra": "mean: 340.1873076599941 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 3.7809436531368963,
            "unit": "iter/sec",
            "range": "stddev: 0.009397519751538977",
            "extra": "mean: 264.4842377300017 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 3.6689491698673935,
            "unit": "iter/sec",
            "range": "stddev: 0.008152412268041835",
            "extra": "mean: 272.5576053800012 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 3.9593094260269437,
            "unit": "iter/sec",
            "range": "stddev: 0.008643702831403963",
            "extra": "mean: 252.56929741999784 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.9035310296408092,
            "unit": "iter/sec",
            "range": "stddev: 0.011606886416724768",
            "extra": "mean: 525.3394793299992 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.8298270646529189,
            "unit": "iter/sec",
            "range": "stddev: 0.008246111058467094",
            "extra": "mean: 546.4997317599955 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.9328540711813105,
            "unit": "iter/sec",
            "range": "stddev: 0.011822773852717667",
            "extra": "mean: 517.3696322500052 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 6.671303614506522,
            "unit": "iter/sec",
            "range": "stddev: 0.007881040850766",
            "extra": "mean: 149.8957411900028 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 5.86616526537297,
            "unit": "iter/sec",
            "range": "stddev: 0.00854960667068648",
            "extra": "mean: 170.46911479000414 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 7.191945247322371,
            "unit": "iter/sec",
            "range": "stddev: 0.00788203748025946",
            "extra": "mean: 139.0444400800061 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 160.46313589164535,
            "unit": "iter/sec",
            "range": "stddev: 0.0032716962366649014",
            "extra": "mean: 6.231960969996635 msec\nrounds: 20"
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
          "id": "d50d0165f1a5bc5810893d414c036a3a69d3df86",
          "message": "Improve metric performance by not executing Python (#46)",
          "timestamp": "2024-07-03T23:44:49+10:00",
          "tree_id": "cdc6b0c5cd02a0248b1463529824f17f788d403b",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/d50d0165f1a5bc5810893d414c036a3a69d3df86"
        },
        "date": 1720014841666,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 3.1406874757178094,
            "unit": "iter/sec",
            "range": "stddev: 0.006028185959351623",
            "extra": "mean: 318.4016263100003 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 3.0237937476206365,
            "unit": "iter/sec",
            "range": "stddev: 0.00524355887474047",
            "extra": "mean: 330.710386840002 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 2.49944904857075,
            "unit": "iter/sec",
            "range": "stddev: 0.0069669016053015",
            "extra": "mean: 400.08817166000085 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 3.172154911082174,
            "unit": "iter/sec",
            "range": "stddev: 0.005351087487189409",
            "extra": "mean: 315.24311644000136 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 3.064216078606707,
            "unit": "iter/sec",
            "range": "stddev: 0.0034749593990289246",
            "extra": "mean: 326.3477425700012 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 3.1776767530869066,
            "unit": "iter/sec",
            "range": "stddev: 0.009072871778033446",
            "extra": "mean: 314.6953191600011 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.77770372290717,
            "unit": "iter/sec",
            "range": "stddev: 0.009830450843263498",
            "extra": "mean: 562.5234324000002 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.7397474219247275,
            "unit": "iter/sec",
            "range": "stddev: 0.008763806181757892",
            "extra": "mean: 574.7960809700032 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.7661220106349467,
            "unit": "iter/sec",
            "range": "stddev: 0.011228879107502714",
            "extra": "mean: 566.2122967599987 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 4.581720870228785,
            "unit": "iter/sec",
            "range": "stddev: 0.01012056865846842",
            "extra": "mean: 218.25860376999913 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 4.241784752034799,
            "unit": "iter/sec",
            "range": "stddev: 0.008494608816920653",
            "extra": "mean: 235.74982193999745 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 4.527550919929089,
            "unit": "iter/sec",
            "range": "stddev: 0.00826953588541545",
            "extra": "mean: 220.86996207999846 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 163.57625724317919,
            "unit": "iter/sec",
            "range": "stddev: 0.0004801291384276231",
            "extra": "mean: 6.113356650001833 msec\nrounds: 20"
          }
        ]
      }
    ]
  }
}