#!/bin/bash

## Remove old files
rm ttbar_delphes/ttbar_10000/*.root

## submot condor job
condor_submit submit.jds 
