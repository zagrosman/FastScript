#!/usr/bin/perl
use strict;
use warnings;
use Bio::AlignIO;
use GD;

# load alignment file (in this case, a FASTA file)
my $infile = "alignment.fasta";
my $informat = "fasta";
my $aln = Bio::AlignIO->new(-file => $infile, -format => $informat)->next_aln;

# set font size and dpi for high resolution image
my $font_size = 18;
my $dpi = 300;

# create image object
my $image_width = 800;
my $image_height = 400;
my $image = GD::Image->new($image_width, $image_height);

# define color palette
my $white = $image->colorAllocate(255, 255, 255);
my $black = $image->colorAllocate(0, 0, 0);
my $red = $image->colorAllocate(255, 0, 0);
my $blue = $image->colorAllocate(0, 0, 255);
my $green = $image->colorAllocate(0, 128, 0);

# set background color
$image->fill(0, 0, $white);

# define color map for residues
my %color_map = (
    A => $green,
    C => $blue,
    G => $black,
    T => $red,
    "-" => $white
);

# calculate size of one cell in the image
my $cell_width = int($image_width / $aln->length);
my $cell_height = int($image_height / scalar($aln->each_seq));

# draw cells for each residue in the alignment
for (my $col = 1; $col <= $aln->length; $col++) {
    for my $seq ($aln->each_seq) {
        my $residue = $seq->subseq($col, $col);
        my $color = $color_map{$residue};
        $image->filledRectangle(($col - 1) * $cell_width, $seq->id - 1 * $cell_height,
                                $col * $cell_width, $seq->id * $cell_height, $color);
    }
}

# create output file and save image
my $outfile = "alignment.png";
open my $out, ">$outfile" or die "Can't open output file: $!";
binmode $out;
print $out $image->png;
close $out;
