/**
 * make.fun entry for the news-image-20261119 bounty.
 *
 * "Sum up 19 November's world news in one image": the program writes one
 * image to /output/entry.png. The front page was drawn by the agent that
 * built this repository (see tools/), and this program carries those exact
 * bytes into the output directory: no network, no randomness, byte for byte
 * the same on every run.
 *
 * Run locally with:
 *   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const baseDir = import.meta.dirname ?? process.cwd();
const sourceImage = join(baseDir, 'entry.png');
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const destination = join(outputDir, 'entry.png');

// The image ships with the repository; nothing is fetched and nothing is
// generated at run time, so both runs of the grader write the same bytes.
if (!existsSync(sourceImage)) {
  console.error(`entry image missing: ${sourceImage}`);
  process.exit(1);
}

mkdirSync(outputDir, { recursive: true });
writeFileSync(destination, readFileSync(sourceImage));
console.log(`wrote ${destination}`);
