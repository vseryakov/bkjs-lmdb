{
    "target_defaults": {
      "defines": [
        "_REENTRANT",
        "_THREAD_SAFE",
        "_POSIX_PTHREAD_SEMANTICS",
      ],
      "include_dirs": [
        ".",
        "bklib",
        "lmdb",
        "<(node_root_dir)/deps/openssl/openssl/include",
        "/opt/local/include",
        "<!(node -e \"require('nan')\")"
      ]
    },
    "targets": [
    {
      "target_name": "binding",
      "libraries": [
        "-L/opt/local/lib",
      ],
      "sources": [
        "binding.cpp",
        "lmdb/mdb.c",
        "lmdb/midl.c",
      ],
      "conditions": [
        [ 'OS=="mac"', {
          "defines": [
            "OS_MACOSX",
          ],
          "xcode_settings": {
            "OTHER_CFLAGS": [
              "-g -fPIC",
            ],
          },
        }],
        [ 'OS=="linux"', {
          "defines": [
            "OS_LINUX",
          ],
          "cflags_cc+": [
            "-g -fPIC -rdynamic",
          ],
        }],
      ]
    }]
}
