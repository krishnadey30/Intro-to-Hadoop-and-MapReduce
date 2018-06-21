# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

run_mapreduce() {
	hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
}

run_mapreduce_with_combiner() {
	hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper $1 -reducer $2 -combiner $2 -file $1 -file $2 -input $3 -output $4
}
alias hs=run_mapreduce
alias hsc=run_mapreduce_with_combiner


# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
