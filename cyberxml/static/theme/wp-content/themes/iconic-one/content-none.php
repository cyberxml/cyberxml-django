<?php
/*
 * "No posts found" template.
 *
 * @package WordPress - Themonic Framework
 * @subpackage Iconic_One
 * @since Iconic One 1.0
 */
?>

	<article id="post-0" class="post no-results not-found">
		<header class="entry-header">
			<h1 class="entry-title"><?php _e( 'Nothing Found', 'themonic' ); ?></h1>
		</header>

		<div class="entry-content">
			<p><?php _e( 'Kindly search your topic below or browse the recent posts.', 'themonic' ); ?></p>
			<?php get_search_form(); ?>
		</div><!-- .entry-content -->
	</article><!-- #post-0 -->
