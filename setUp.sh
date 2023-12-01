exp=01-tfm-deen
conf_url=https://raw.githubusercontent.com/isi-nlp/rtg/master/experiments/transformer.base.yml

[[ -d $exp ]] ||  mkdir -p $exp
[[ -f $exp/conf.yml ]] || curl $conf_url > $exp/conf.yml