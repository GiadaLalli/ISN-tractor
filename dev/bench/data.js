window.BENCHMARK_DATA = {
  "lastUpdate": 1720173689218,
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
      },
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
          "id": "9f840a9ade61247dbbd7e2368c18d607d4ff0e44",
          "message": "Link to performance history plots from the README",
          "timestamp": "2024-07-03T15:47:05+02:00",
          "tree_id": "f9371040b50489b772d2b1bfa99266f7a4354c2a",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/9f840a9ade61247dbbd7e2368c18d607d4ff0e44"
        },
        "date": 1720015157166,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 2.3535848592244193,
            "unit": "iter/sec",
            "range": "stddev: 0.011177292273248998",
            "extra": "mean: 424.88376659999915 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 2.2330451268519935,
            "unit": "iter/sec",
            "range": "stddev: 0.010151863870796762",
            "extra": "mean: 447.818984029999 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 1.87037316083966,
            "unit": "iter/sec",
            "range": "stddev: 0.00897994017372864",
            "extra": "mean: 534.6526676800011 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 2.326630025898117,
            "unit": "iter/sec",
            "range": "stddev: 0.008005664119222367",
            "extra": "mean: 429.80619560000036 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 2.274876410359113,
            "unit": "iter/sec",
            "range": "stddev: 0.006020490711195479",
            "extra": "mean: 439.584320030001 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 2.32076117697488,
            "unit": "iter/sec",
            "range": "stddev: 0.012479098114974807",
            "extra": "mean: 430.8931095199995 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.3164258123567698,
            "unit": "iter/sec",
            "range": "stddev: 0.018710678139777476",
            "extra": "mean: 759.6326284500003 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.2902365371844902,
            "unit": "iter/sec",
            "range": "stddev: 0.016686609802659094",
            "extra": "mean: 775.0516832999983 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.306461279432989,
            "unit": "iter/sec",
            "range": "stddev: 0.01936214463384477",
            "extra": "mean: 765.4264353200006 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 3.3768871553921787,
            "unit": "iter/sec",
            "range": "stddev: 0.01373885788943786",
            "extra": "mean: 296.13071269000216 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 3.173535970471738,
            "unit": "iter/sec",
            "range": "stddev: 0.011650823285466422",
            "extra": "mean: 315.10592893999956 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 3.405611334921201,
            "unit": "iter/sec",
            "range": "stddev: 0.012169941952006134",
            "extra": "mean: 293.6330372600014 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 162.05735126348847,
            "unit": "iter/sec",
            "range": "stddev: 0.0007885596707887205",
            "extra": "mean: 6.170654970005671 msec\nrounds: 20"
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
          "id": "29a2010de5889eeb60a02292eb92ca3538e153f3",
          "message": "Prepare for 0.3.0 release (#47)",
          "timestamp": "2024-07-03T23:55:10+10:00",
          "tree_id": "d927a7e670e5fce863c048b5d1be6d5671349aa2",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/29a2010de5889eeb60a02292eb92ca3538e153f3"
        },
        "date": 1720015452101,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 3.3135056316316387,
            "unit": "iter/sec",
            "range": "stddev: 0.007320391292800441",
            "extra": "mean: 301.79517138999984 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 3.2265354901171164,
            "unit": "iter/sec",
            "range": "stddev: 0.006223936731555036",
            "extra": "mean: 309.92995522999877 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 2.638845353460127,
            "unit": "iter/sec",
            "range": "stddev: 0.0078057988956529364",
            "extra": "mean: 378.95362026000214 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 3.4118186026216417,
            "unit": "iter/sec",
            "range": "stddev: 0.00546218445882285",
            "extra": "mean: 293.0988181000009 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 3.2957859469184942,
            "unit": "iter/sec",
            "range": "stddev: 0.004948036711398716",
            "extra": "mean: 303.41776319999894 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 3.3572458931991305,
            "unit": "iter/sec",
            "range": "stddev: 0.012526924804510656",
            "extra": "mean: 297.8631985300001 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.905813425049385,
            "unit": "iter/sec",
            "range": "stddev: 0.009338545966638514",
            "extra": "mean: 524.7103346299951 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.8444055719083554,
            "unit": "iter/sec",
            "range": "stddev: 0.013249324820125563",
            "extra": "mean: 542.1801014000016 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.8957772748225292,
            "unit": "iter/sec",
            "range": "stddev: 0.013543351939695603",
            "extra": "mean: 527.4881249400005 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 4.752161726731916,
            "unit": "iter/sec",
            "range": "stddev: 0.011724360426213666",
            "extra": "mean: 210.4305487700026 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 4.352616031326689,
            "unit": "iter/sec",
            "range": "stddev: 0.012943263847938907",
            "extra": "mean: 229.7468907899963 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 4.658749142221515,
            "unit": "iter/sec",
            "range": "stddev: 0.014906940878521856",
            "extra": "mean: 214.6498919499993 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 153.90648281970982,
            "unit": "iter/sec",
            "range": "stddev: 0.0006832168491410662",
            "extra": "mean: 6.497452099996508 msec\nrounds: 20"
          }
        ]
      },
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
          "id": "4a52a838cd26ca715e9e3208837b9749946b5e75",
          "message": "Try the new way of publishing packages to PyPI",
          "timestamp": "2024-07-03T16:18:52+02:00",
          "tree_id": "31a10898be3b7afb519e852d1996988e32c55f96",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/4a52a838cd26ca715e9e3208837b9749946b5e75"
        },
        "date": 1720016996512,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 3.1165560269616663,
            "unit": "iter/sec",
            "range": "stddev: 0.004912432523817183",
            "extra": "mean: 320.86700555000164 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 3.0018073341033142,
            "unit": "iter/sec",
            "range": "stddev: 0.006873888567210831",
            "extra": "mean: 333.1326393399979 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 2.4601326860696524,
            "unit": "iter/sec",
            "range": "stddev: 0.009076709325225587",
            "extra": "mean: 406.4821404400004 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 3.0483838778204535,
            "unit": "iter/sec",
            "range": "stddev: 0.004123774073518433",
            "extra": "mean: 328.04267444000004 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 2.9414098532060438,
            "unit": "iter/sec",
            "range": "stddev: 0.0076207817446722805",
            "extra": "mean: 339.97302311 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 3.1467391373914864,
            "unit": "iter/sec",
            "range": "stddev: 0.006058388661962547",
            "extra": "mean: 317.7892911799984 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.7464877680347302,
            "unit": "iter/sec",
            "range": "stddev: 0.009855219763610852",
            "extra": "mean: 572.5777290300005 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.703656629865147,
            "unit": "iter/sec",
            "range": "stddev: 0.009021001587896463",
            "extra": "mean: 586.9727399699991 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.7242100788215646,
            "unit": "iter/sec",
            "range": "stddev: 0.014060443167240023",
            "extra": "mean: 579.9757305000003 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 4.557597523446164,
            "unit": "iter/sec",
            "range": "stddev: 0.009676763442357553",
            "extra": "mean: 219.4138457500003 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 4.178569414093508,
            "unit": "iter/sec",
            "range": "stddev: 0.009980980335597835",
            "extra": "mean: 239.31635469000298 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 4.491475678389915,
            "unit": "iter/sec",
            "range": "stddev: 0.008760334235978842",
            "extra": "mean: 222.6439753000011 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 172.40225315069853,
            "unit": "iter/sec",
            "range": "stddev: 0.0006587611234419841",
            "extra": "mean: 5.800388229995406 msec\nrounds: 20"
          }
        ]
      },
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
          "id": "c4ff5ee1bea746a69dbc316fa5ad9052c395cc6a",
          "message": "Remove print()s",
          "timestamp": "2024-07-03T16:41:29+02:00",
          "tree_id": "840913c0da15248a4ae1b515989be296cc5375d4",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/c4ff5ee1bea746a69dbc316fa5ad9052c395cc6a"
        },
        "date": 1720018258850,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 3.339110767966056,
            "unit": "iter/sec",
            "range": "stddev: 0.00925827143563896",
            "extra": "mean: 299.48093055000015 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 3.1488091688986217,
            "unit": "iter/sec",
            "range": "stddev: 0.01092321583011237",
            "extra": "mean: 317.5803760599999 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 2.4086272668698587,
            "unit": "iter/sec",
            "range": "stddev: 0.011149285298047259",
            "extra": "mean: 415.17424208999927 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 3.2548489963089065,
            "unit": "iter/sec",
            "range": "stddev: 0.007519798804354698",
            "extra": "mean: 307.23391504000006 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 3.0936185571601302,
            "unit": "iter/sec",
            "range": "stddev: 0.009430060217032259",
            "extra": "mean: 323.2460568500005 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 3.2090311581096334,
            "unit": "iter/sec",
            "range": "stddev: 0.014836337786063422",
            "extra": "mean: 311.62053302999936 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.628399947698455,
            "unit": "iter/sec",
            "range": "stddev: 0.013962263829903971",
            "extra": "mean: 614.0997495199986 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.6231738602397332,
            "unit": "iter/sec",
            "range": "stddev: 0.012557139463678861",
            "extra": "mean: 616.0769493000004 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.6263594927291554,
            "unit": "iter/sec",
            "range": "stddev: 0.02291224259750806",
            "extra": "mean: 614.8702082599976 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 5.537504613670989,
            "unit": "iter/sec",
            "range": "stddev: 0.009361567624250807",
            "extra": "mean: 180.58675698999878 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 4.980258070497891,
            "unit": "iter/sec",
            "range": "stddev: 0.0077550482423643955",
            "extra": "mean: 200.79280748999963 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 5.850174979748643,
            "unit": "iter/sec",
            "range": "stddev: 0.006686909464815697",
            "extra": "mean: 170.9350580900002 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 162.7926429328855,
            "unit": "iter/sec",
            "range": "stddev: 0.00041878807877892936",
            "extra": "mean: 6.142783740001505 msec\nrounds: 20"
          }
        ]
      },
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
          "id": "1d6a19f1ecf2123fac4d912226d9d0fcbf438300",
          "message": "Fix bug causing incorrect shaped output",
          "timestamp": "2024-07-03T16:53:13+02:00",
          "tree_id": "102bc1076154c500992dde9058019140b002ae7d",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/1d6a19f1ecf2123fac4d912226d9d0fcbf438300"
        },
        "date": 1720018855735,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 4.4663955637808535,
            "unit": "iter/sec",
            "range": "stddev: 0.0035628871547985098",
            "extra": "mean: 223.894186199999 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 4.242899309162653,
            "unit": "iter/sec",
            "range": "stddev: 0.0035791783311780014",
            "extra": "mean: 235.6878933799993 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 3.3503405180382533,
            "unit": "iter/sec",
            "range": "stddev: 0.006747310783882466",
            "extra": "mean: 298.47712333000004 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 4.310865897741394,
            "unit": "iter/sec",
            "range": "stddev: 0.004380978531155283",
            "extra": "mean: 231.97195730999965 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 4.1336263077465,
            "unit": "iter/sec",
            "range": "stddev: 0.0016773222557081213",
            "extra": "mean: 241.91833648000056 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 4.423091518981259,
            "unit": "iter/sec",
            "range": "stddev: 0.012386079994632537",
            "extra": "mean: 226.08621044999836 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 2.160167646959531,
            "unit": "iter/sec",
            "range": "stddev: 0.009383517101131281",
            "extra": "mean: 462.92703319000054 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 2.0932411586308537,
            "unit": "iter/sec",
            "range": "stddev: 0.009563922755585211",
            "extra": "mean: 477.728041929999 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 2.194213782366808,
            "unit": "iter/sec",
            "range": "stddev: 0.013000066030643007",
            "extra": "mean: 455.74410663000265 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 7.639424935559173,
            "unit": "iter/sec",
            "range": "stddev: 0.008461205300788971",
            "extra": "mean: 130.89990521999994 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 6.683263276738827,
            "unit": "iter/sec",
            "range": "stddev: 0.008875323818285081",
            "extra": "mean: 149.627503600002 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 7.7827143337638525,
            "unit": "iter/sec",
            "range": "stddev: 0.009469375537639576",
            "extra": "mean: 128.48987603999376 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 177.8710229856741,
            "unit": "iter/sec",
            "range": "stddev: 0.0003387924393473743",
            "extra": "mean: 5.6220512099969255 msec\nrounds: 20"
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
          "id": "bafe27e2f9412e13b39047d22f18618d860074c4",
          "message": "Updating tutorial folder",
          "timestamp": "2024-07-03T17:20:26+02:00",
          "tree_id": "ec01365bd48442345da2bce542074c064bbab602",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/bafe27e2f9412e13b39047d22f18618d860074c4"
        },
        "date": 1720020454214,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 4.7500168614554905,
            "unit": "iter/sec",
            "range": "stddev: 0.0029306236976488383",
            "extra": "mean: 210.52556846999948 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 4.501775670041204,
            "unit": "iter/sec",
            "range": "stddev: 0.003489742388250897",
            "extra": "mean: 222.13456940000015 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 3.5440028254778047,
            "unit": "iter/sec",
            "range": "stddev: 0.006856176511071365",
            "extra": "mean: 282.16681792999964 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 4.679064132383558,
            "unit": "iter/sec",
            "range": "stddev: 0.004598835590066284",
            "extra": "mean: 213.7179512199998 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 4.481595952679319,
            "unit": "iter/sec",
            "range": "stddev: 0.001694873771667802",
            "extra": "mean: 223.13479629999904 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 4.862012258409687,
            "unit": "iter/sec",
            "range": "stddev: 0.009981820645462998",
            "extra": "mean: 205.67615769999918 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 2.3456207848580206,
            "unit": "iter/sec",
            "range": "stddev: 0.00956960558002482",
            "extra": "mean: 426.32637230000057 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 2.2671250680802566,
            "unit": "iter/sec",
            "range": "stddev: 0.008883106743167689",
            "extra": "mean: 441.0872669000014 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 2.3739200144844697,
            "unit": "iter/sec",
            "range": "stddev: 0.009576053197670131",
            "extra": "mean: 421.2441842600009 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 7.956657537715596,
            "unit": "iter/sec",
            "range": "stddev: 0.007730419764614313",
            "extra": "mean: 125.68091503999881 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 7.03971919296779,
            "unit": "iter/sec",
            "range": "stddev: 0.00792442661771607",
            "extra": "mean: 142.0511205899993 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 8.160064672964761,
            "unit": "iter/sec",
            "range": "stddev: 0.008839696698133889",
            "extra": "mean: 122.54804833999856 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 171.7803079035637,
            "unit": "iter/sec",
            "range": "stddev: 0.0003788444479531565",
            "extra": "mean: 5.821389030001001 msec\nrounds: 20"
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
          "id": "d8b395c0da8163f40da5b0da757e7aa320abbaa4",
          "message": "Update README.md",
          "timestamp": "2024-07-03T17:21:38+02:00",
          "tree_id": "5a00f2583cee35d97e12fbd89596633cdc93109f",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/d8b395c0da8163f40da5b0da757e7aa320abbaa4"
        },
        "date": 1720020643252,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 3.410831828353586,
            "unit": "iter/sec",
            "range": "stddev: 0.00495443225656851",
            "extra": "mean: 293.1836133600001 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 3.229151447514439,
            "unit": "iter/sec",
            "range": "stddev: 0.005091286291555903",
            "extra": "mean: 309.6788788799998 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 2.516606959595279,
            "unit": "iter/sec",
            "range": "stddev: 0.008230824430630633",
            "extra": "mean: 397.3604206200002 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 3.3225800718382956,
            "unit": "iter/sec",
            "range": "stddev: 0.004650050464646813",
            "extra": "mean: 300.9709257200012 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 3.185504279189919,
            "unit": "iter/sec",
            "range": "stddev: 0.006742480232185225",
            "extra": "mean: 313.9220394499995 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 3.3864147432729528,
            "unit": "iter/sec",
            "range": "stddev: 0.012268691497521472",
            "extra": "mean: 295.29755679999937 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.6652425327407208,
            "unit": "iter/sec",
            "range": "stddev: 0.011015591094449207",
            "extra": "mean: 600.5131266699999 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.6194368933979288,
            "unit": "iter/sec",
            "range": "stddev: 0.011896418084558835",
            "extra": "mean: 617.4985910700008 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.6943588916511028,
            "unit": "iter/sec",
            "range": "stddev: 0.013823479627881913",
            "extra": "mean: 590.1937334100035 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 5.624131304376893,
            "unit": "iter/sec",
            "range": "stddev: 0.010772390079047041",
            "extra": "mean: 177.80523708999567 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 4.870105652897118,
            "unit": "iter/sec",
            "range": "stddev: 0.011479131358188953",
            "extra": "mean: 205.33435437999628 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 5.690964079424347,
            "unit": "iter/sec",
            "range": "stddev: 0.010764388416037985",
            "extra": "mean: 175.71715196999662 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 163.80372562558978,
            "unit": "iter/sec",
            "range": "stddev: 0.0005840298369739793",
            "extra": "mean: 6.104867250002144 msec\nrounds: 20"
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
          "id": "65c88506ad248cd6cbca165961074bac78ca1684",
          "message": "Update test_benchmark.py",
          "timestamp": "2024-07-04T11:05:53+02:00",
          "tree_id": "62536a1d11adc483e1486c3db84e761862ee1b53",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/65c88506ad248cd6cbca165961074bac78ca1684"
        },
        "date": 1720084456074,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 3.6426401503930883,
            "unit": "iter/sec",
            "range": "stddev: 0.007175247439904838",
            "extra": "mean: 274.526156500001 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 3.502160309758404,
            "unit": "iter/sec",
            "range": "stddev: 0.00594115906567146",
            "extra": "mean: 285.5380426800008 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 2.7352957687351536,
            "unit": "iter/sec",
            "range": "stddev: 0.008474395512309557",
            "extra": "mean: 365.5911771699982 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 3.6681125186183094,
            "unit": "iter/sec",
            "range": "stddev: 0.0034108526495968627",
            "extra": "mean: 272.61977241000125 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 3.4978192640825774,
            "unit": "iter/sec",
            "range": "stddev: 0.0058377393754264414",
            "extra": "mean: 285.8924159600008 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 3.8101424763644998,
            "unit": "iter/sec",
            "range": "stddev: 0.01125063823816365",
            "extra": "mean: 262.45737691000045 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.8578355743464248,
            "unit": "iter/sec",
            "range": "stddev: 0.010633964797193791",
            "extra": "mean: 538.2607663500005 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.8086173541178432,
            "unit": "iter/sec",
            "range": "stddev: 0.010955377566363014",
            "extra": "mean: 552.9085506800038 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.8789780957620428,
            "unit": "iter/sec",
            "range": "stddev: 0.011158351887088126",
            "extra": "mean: 532.2041817599995 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 6.301743719691925,
            "unit": "iter/sec",
            "range": "stddev: 0.010138130226579415",
            "extra": "mean: 158.6862374099985 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 5.555334905368851,
            "unit": "iter/sec",
            "range": "stddev: 0.009145865857904955",
            "extra": "mean: 180.0071493500002 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 6.534296892349359,
            "unit": "iter/sec",
            "range": "stddev: 0.009817532214322137",
            "extra": "mean: 153.0386538099981 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 166.95084427217373,
            "unit": "iter/sec",
            "range": "stddev: 0.000477340809376724",
            "extra": "mean: 5.98978702000295 msec\nrounds: 20"
          }
        ]
      },
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
          "id": "d316b0218591f6bc92d5fb5f8994a9de3d274847",
          "message": "Fix biweight_midcorrelation implementation\n\nThanks to @FedericoMelograna",
          "timestamp": "2024-07-05T11:22:43+02:00",
          "tree_id": "886ec486d8f5c52a0b3d958cd0629d8377f60fe9",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/d316b0218591f6bc92d5fb5f8994a9de3d274847"
        },
        "date": 1720171913858,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 3.4407509767006488,
            "unit": "iter/sec",
            "range": "stddev: 0.005804446953347532",
            "extra": "mean: 290.63422688000054 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 3.267849410843593,
            "unit": "iter/sec",
            "range": "stddev: 0.003999211556271975",
            "extra": "mean: 306.01165300999924 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 2.5796081559491015,
            "unit": "iter/sec",
            "range": "stddev: 0.00998816873079212",
            "extra": "mean: 387.6557754299995 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 3.3912478060026094,
            "unit": "iter/sec",
            "range": "stddev: 0.0033235270593326154",
            "extra": "mean: 294.8767112299993 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 3.2205351296828595,
            "unit": "iter/sec",
            "range": "stddev: 0.005231922290260578",
            "extra": "mean: 310.5074031900017 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 3.4811596109522642,
            "unit": "iter/sec",
            "range": "stddev: 0.012934737123068116",
            "extra": "mean: 287.2606004199997 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 1.7287804514722267,
            "unit": "iter/sec",
            "range": "stddev: 0.010283709296214584",
            "extra": "mean: 578.442450079998 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 1.6677452867679883,
            "unit": "iter/sec",
            "range": "stddev: 0.01281798819559359",
            "extra": "mean: 599.6119479000015 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 1.7388592668772995,
            "unit": "iter/sec",
            "range": "stddev: 0.014508318900236",
            "extra": "mean: 575.0896688700016 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 5.593053534806872,
            "unit": "iter/sec",
            "range": "stddev: 0.013451998895985006",
            "extra": "mean: 178.79321086000118 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 4.964988805499399,
            "unit": "iter/sec",
            "range": "stddev: 0.011263960320698322",
            "extra": "mean: 201.4103231999968 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 5.814054465315108,
            "unit": "iter/sec",
            "range": "stddev: 0.011976527723715772",
            "extra": "mean: 171.99701275000052 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 156.8010739442821,
            "unit": "iter/sec",
            "range": "stddev: 0.0009263890474040519",
            "extra": "mean: 6.377507340002921 msec\nrounds: 20"
          }
        ]
      },
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
          "id": "944a6e1945a57f22d8072cee5c1b6bbf91eb3178",
          "message": "Prepare bugfix release",
          "timestamp": "2024-07-05T11:53:44+02:00",
          "tree_id": "79aba53f4ad798427a52a13de42737f951fb8fdb",
          "url": "https://github.com/GiadaLalli/ISN-tractor/commit/944a6e1945a57f22d8072cee5c1b6bbf91eb3178"
        },
        "date": 1720173688865,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/test_benchmark.py::test_regression_biweight_max",
            "value": 4.457436282180501,
            "unit": "iter/sec",
            "range": "stddev: 0.006178939071722618",
            "extra": "mean: 224.34420520999964 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_avg",
            "value": 4.308686704909861,
            "unit": "iter/sec",
            "range": "stddev: 0.0038791527285250197",
            "extra": "mean: 232.0892811399989 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_biweight_none",
            "value": 3.423096200634209,
            "unit": "iter/sec",
            "range": "stddev: 0.007966908062849273",
            "extra": "mean: 292.1331862699992 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_max",
            "value": 4.483667906067235,
            "unit": "iter/sec",
            "range": "stddev: 0.006795913856575834",
            "extra": "mean: 223.0316832000011 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_avg",
            "value": 4.332277240867986,
            "unit": "iter/sec",
            "range": "stddev: 0.0028101126483123964",
            "extra": "mean: 230.8254860900007 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_pearson_none",
            "value": 4.726949373975331,
            "unit": "iter/sec",
            "range": "stddev: 0.00993142421265107",
            "extra": "mean: 211.55293210999787 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_max",
            "value": 2.2840692580519026,
            "unit": "iter/sec",
            "range": "stddev: 0.009692139760266224",
            "extra": "mean: 437.8150953500011 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_avg",
            "value": 2.2012032578950063,
            "unit": "iter/sec",
            "range": "stddev: 0.010033319946726498",
            "extra": "mean: 454.29698343999917 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_spearman_none",
            "value": 2.284146258047259,
            "unit": "iter/sec",
            "range": "stddev: 0.012169034320513616",
            "extra": "mean: 437.8003363299996 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_max",
            "value": 7.7442954322965845,
            "unit": "iter/sec",
            "range": "stddev: 0.010237334373875275",
            "extra": "mean: 129.12730521999833 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_avg",
            "value": 6.761349443111727,
            "unit": "iter/sec",
            "range": "stddev: 0.011005642071310716",
            "extra": "mean: 147.89947013000074 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dot_none",
            "value": 7.982801491643748,
            "unit": "iter/sec",
            "range": "stddev: 0.009308660517533865",
            "extra": "mean: 125.26930565000043 msec\nrounds: 20"
          },
          {
            "name": "test/test_benchmark.py::test_regression_dense",
            "value": 161.71118820678188,
            "unit": "iter/sec",
            "range": "stddev: 0.00047297259958633804",
            "extra": "mean: 6.183864029997039 msec\nrounds: 20"
          }
        ]
      }
    ]
  }
}