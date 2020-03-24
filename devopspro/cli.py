import argparse
import os.path

import yaml

import devopspro.config as c


def load_config(path):
    with open(path, 'r') as conf_file:
        conf = yaml.safe_load(conf_file)
    return conf


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', dest='config', action='store', type=str,
        help='path to custom config',
        default=os.path.join(os.path.dirname(__file__), "config.yaml")
    )
    return parser


def business_logic(conf):
    print(c.HELLO + ", {}!!!".format(conf.get('name', 'World')))


def main():
    parser = build_parser()
    params, other_params = parser.parse_known_args()
    conf = load_config(params.config)
    # here goes nothing
    business_logic(conf)


if __name__ == "__main__":
    main()
