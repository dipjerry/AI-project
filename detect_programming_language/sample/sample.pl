#!/usr/bin/perl

use strict;
use warnings;

sub greet {
    my ($name) = @_;
    print "Hello, $name!\n";
}

greet("Alice");
