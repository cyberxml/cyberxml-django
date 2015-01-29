<?php
/*
 * Iconic One Theme's Functions file, this is the heart of theme, modification directly is not recommended.
 * Iconic One Supports Child Themes, it is the way to go.
 * If you want to change design use custom.css, details at themonic.com/iconic-one/
 * Use a child theme for customization (see http://codex.wordpress.org/Theme_Development and
 * http://codex.wordpress.org/Child_Themes).
 * @package WordPress - Themonic Framework
 * @subpackage Iconic_One
 * @since Iconic One 1.0
 * © 2013 Shashank Singh, Themonic.com
 */

/*
 * Primary content width according to the design and stylesheet.
 */
if ( ! isset( $content_width ) )
	$content_width = 665;

/*
 * Iconic One supported features and Registering defaults
 */
if( !function_exists( 'themonic_setup' ) ) :

function themonic_setup() {
	/*
	 * Making Iconic One ready for translation.
	 * Translations can be added to the /languages/ directory. Sample iconic-one.pot file is included.
	 */
	load_theme_textdomain( 'themonic', get_template_directory() . '/languages' );

	// Adds RSS feed links to <head> for posts and comments.
	add_theme_support( 'automatic-feed-links' );

	// Adds support for Navigation menu, Iconic One uses wp_nav_menu() in one location.
	register_nav_menu( 'primary', __( 'Primary Menu', 'themonic' ) );
	
	// Iconic One supports custom background color and image using default wordpress funtions.
	add_theme_support( 'custom-background', array(
		'default-color' => 'e8e8e8',
	) );

	// Uncomment the following two lines to add support for post thumbnails - for classic blog layout
	add_theme_support( 'post-thumbnails' );
	set_post_thumbnail_size( 660, 9999 ); // Unlimited height, soft crop
	//Defining home page thumbnail size
	add_image_size('excerpt-thumbnail', 200, 140, true);
}
endif; //Iconic One setup
add_action( 'after_setup_theme', 'themonic_setup' );


 /*
 * Loads the Themonic Customizer for live customization, to learn more visit Themonic.com
 */
 require_once( get_template_directory() . '/inc/themonic-customizer.php' );
 
 /* Adding Read More button after excerpts */
	if( !function_exists( 'io_excerpt_more' ) ) :
		function io_excerpt_more($more) {
		global $post;
		return '… <span class="read-more"><a href="'. get_permalink($post->ID) . '">' . __( 'Read More', 'themonic' ) . ' &raquo;</a></span>';
		}
		add_filter('excerpt_more', 'io_excerpt_more');
	endif; //io_excerpt_more
/*
 * Enqueueing scripts and styles for front-end of the Themonic Framework.
 * @since Iconic One 1.0
 */ 
function themonic_scripts_styles() {
	global $wp_styles;

	/*
	 * Adds JavaScript to pages with the comment form to support
	 * sites with threaded comments (when in use).
	 */
	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) )
		wp_enqueue_script( 'comment-reply' );

 /*
	 * Adds Selectnav.js JavaScript for handling the navigation menu and creating a select based navigation for reposive layout.
 */
   wp_enqueue_script('themonic-mobile-navigation', get_template_directory_uri() . '/js/selectnav.js', array(), '1.0', true );
/*
     * Loads the awesome readable ubuntu font CSS file for Iconic One.
*/
    if ( 'off' !== _x( 'on', 'Ubuntu font: on or off', 'themonic' ) ) {
        $subsets = 'latin,latin-ext';
        $protocol = is_ssl() ? 'https' : 'http';
        $query_args = array(
            'family' => 'Ubuntu:400,700',
            'subset' => $subsets,
        );
        wp_enqueue_style( 'themonic-fonts', add_query_arg( $query_args, "$protocol://fonts.googleapis.com/css" ), array(), null );
    }
	/*
	 * Loads Themonic's main stylesheet and the custom stylesheet.
	 */
	wp_enqueue_style( 'themonic-style', get_stylesheet_uri() );
	wp_enqueue_style( 'custom-style', get_template_directory_uri() . '/custom.css' );

	/*
	 * Loads the Internet Explorer specific stylesheet.
	 */
	wp_enqueue_style( 'themonic-ie', get_template_directory_uri() . '/css/ie.css', array( 'themonic-style' ), '20130305' );
	$wp_styles->add_data( 'themonic-ie', 'conditional', 'lt IE 9' );
}
add_action( 'wp_enqueue_scripts', 'themonic_scripts_styles' );

/*
 * WP Title Filter, refer http://codex.wordpress.org/Plugin_API/Filter_Reference/wp_title
 * @since Iconic One 1.0
 */
function themonic_wp_title( $title, $sep ) {
	global $paged, $page;

	if ( is_feed() )
		return $title;

	// Add the site name.
	$title .= get_bloginfo( 'name' );

	// Add the site description for the home/front page.
	$site_description = get_bloginfo( 'description', 'display' );
	if ( $site_description && ( is_home() || is_front_page() ) )
		$title = "$title $sep $site_description";

	// Add a page number if necessary.
	if ( $paged >= 2 || $page >= 2 )
		$title = "$title $sep " . sprintf( __( 'Page %s', 'themonic' ), max( $paged, $page ) );

	return $title;
}
add_filter( 'wp_title', 'themonic_wp_title', 10, 2 );

/*
 * Default Nav Menu fallback to Pages menu, 
 * Makes our wp_nav_menu() fallback -- wp_page_menu() -- show a home link.
 * @since Iconic One 1.0
 */
function themonic_page_menu_args( $args ) {
	if ( ! isset( $args['show_home'] ) )
		$args['show_home'] = true;
	return $args;
}
add_filter( 'wp_page_menu_args', 'themonic_page_menu_args' );

/**
 * Registers the main widgetized sidebar area.
 *
 * @since Iconic O-n-e 1.0
 */
function themonic_widgets_init() {
	register_sidebar( array(
		'name' => __( 'Main Sidebar', 'themonic' ),
		'id' => 'themonic-sidebar',
		'description' => __( 'This is a Sitewide sidebar which appears on posts and pages', 'themonic' ),
		'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget' => '</aside>',
		'before_title' => '<p class="widget-title">',
		'after_title' => '</p>',
	) );
}
add_action( 'widgets_init', 'themonic_widgets_init' );

if ( ! function_exists( 'themonic_content_nav' ) ) :
/**
 * Displays navigation to next/previous pages when applicable.
 *
 * @since Iconic One 1.0
 */
function themonic_content_nav( $html_id ) {
	global $wp_query;

	$html_id = esc_attr( $html_id );

	if ( $wp_query->max_num_pages > 1 ) : ?>
		<nav id="<?php echo $html_id; ?>" class="navigation" role="navigation">
			<div class="assistive-text"><?php _e( 'Post navigation', 'themonic' ); ?></div>
			<div class="nav-previous alignleft"><?php next_posts_link( __( '<span class="meta-nav">&larr;</span> Older posts', 'themonic' ) ); ?></div>
			<div class="nav-next alignright"><?php previous_posts_link( __( 'Newer posts <span class="meta-nav">&rarr;</span>', 'themonic' ) ); ?></div>
		</nav><!-- #<?php echo $html_id; ?> .navigation -->
	<?php endif;
}
endif;

if ( ! function_exists( 'themonic_comment' ) ) :
/**
 * Template for comments and pingbacks.
 *
 * To override this walker in a child theme without modifying the comments template
 * simply create your own themonic_comment(), and that function will be used instead.
 *
 * Used as a callback by wp_list_comments() for displaying the comments.
 *
 * @since Iconic One 1.0
 */
function themonic_comment( $comment, $args, $depth ) {
	$GLOBALS['comment'] = $comment;
	switch ( $comment->comment_type ) :
		case 'pingback' :
		case 'trackback' :
		// Display trackbacks differently than normal comments.
	?>
	<li <?php comment_class(); ?> id="comment-<?php comment_ID(); ?>">
		<p><?php _e( 'Pingback:', 'themonic' ); ?> <?php comment_author_link(); ?> <?php edit_comment_link( __( '(Edit)', 'themonic' ), '<span class="edit-link">', '</span>' ); ?></p>
	<?php
			break;
		default :
		// Proceed with normal comments.
		global $post;
	?>
	<li <?php comment_class(); ?> id="li-comment-<?php comment_ID(); ?>">
		<article id="comment-<?php comment_ID(); ?>" class="comment">
			<header class="comment-meta comment-author vcard">
				<?php
					echo get_avatar( $comment, 30 );
					printf( '<cite class="fn">%1$s %2$s</cite>',
						get_comment_author_link(),
						// Adds Post Author to comments posted by the article writer
						( $comment->user_id === $post->post_author ) ? '<span> ' . __( 'Post author', 'themonic' ) . '</span>' : ''
					);
					printf( '<a href="%1$s"><time datetime="%2$s">%3$s</time></a>',
						esc_url( get_comment_link( $comment->comment_ID ) ),
						get_comment_time( 'c' ),
						/* translators: 1: date */
						sprintf( __( '%1$s', 'themonic' ), get_comment_date() )
					);
				?>
			</header><!-- .comment-meta -->

			<?php if ( '0' == $comment->comment_approved ) : ?>
				<p class="comment-awaiting-moderation"><?php _e( 'Your comment is awaiting moderation.', 'themonic' ); ?></p>
			<?php endif; ?>

			<section class="comment-content comment">
				<?php comment_text(); ?>
				<?php edit_comment_link( __( 'Edit', 'themonic' ), '<p class="edit-link">', '</p>' ); ?>
			</section><!-- .comment-content -->

			<div class="reply">
				<?php comment_reply_link( array_merge( $args, array( 'reply_text' => __( 'Reply', 'themonic' ), 'after' => ' <span>&darr;</span>', 'depth' => $depth, 'max_depth' => $args['max_depth'] ) ) ); ?>
			</div><!-- .reply -->
		</article><!-- #comment-## -->
	<?php
		break;
	endswitch; // end comment_type check
}
endif;

if ( ! function_exists( 'themonic_entry_meta' ) ) :
/**
 * For Meta information for categories, tags, permalink, author, and date.
 *
 * Create your own themonic_entry_meta() to override in a child theme.
 *
 * @since Iconic One 1.0
 */
function themonic_entry_meta() {
	// Translators: used between list items, there is a space after the comma.
	$categories_list = get_the_category_list( __( ', ', 'themonic' ) );

	// Translators: used between list items, there is a space after the comma.
	$tag_list = get_the_tag_list( '', __( ', ', 'themonic' ) );

	$date = sprintf( '<a href="%1$s" title="%2$s" rel="bookmark"><time class="entry-date" datetime="%3$s">%4$s</time></a>',
		esc_url( get_permalink() ),
		esc_attr( get_the_time() ),
		esc_attr( get_the_date( 'c' ) ),
		esc_html( get_the_date() )
	);

	$author = sprintf( '<span class="author vcard"><a class="url fn n" href="%1$s" title="%2$s" rel="author">%3$s</a></span>',
		esc_url( get_author_posts_url( get_the_author_meta( 'ID' ) ) ),
		esc_attr( sprintf( __( 'View all posts by %s', 'themonic' ), get_the_author() ) ),
		get_the_author()
	);

	// Translators: 1 is category, 2 is tag, 3 is the date and 4 is the author's name.
	if ( $tag_list ) {
		$utility_text = __( 'This entry was posted in %1$s and tagged %2$s on %3$s<span class="by-author"> by %4$s</span>.', 'themonic' );
	} elseif ( $categories_list ) {
		$utility_text = __( 'This entry was posted in %1$s on %3$s<span class="by-author"> by %4$s</span>.', 'themonic' );
	} else {
		$utility_text = __( 'This entry was posted on %3$s<span class="by-author"> by %4$s</span>.', 'themonic' );
	}

	printf(
		$utility_text,
		$categories_list,
		$tag_list,
		$date,
		$author
	);
}
endif;

/*
 * WordPress body class Extender :
 * 1. Using a full-width layout without widgets.
 * 2. White or empty background color.
 * 3. Custom fonts enabled.
 * 4. Single or multiple authors.
 *
 * @since Iconic One 1.0
 */
function themonic_body_class( $classes ) {
	$background_color = get_background_color();

	if ( is_page_template( 'page-templates/full-width.php' ) )
		$classes[] = 'full-width';

	if ( empty( $background_color ) )
		$classes[] = 'custom-background-empty';
	elseif ( in_array( $background_color, array( 'fff', 'ffffff' ) ) )
		$classes[] = 'custom-background-white';

	// Enable custom font class only if the font CSS is queued to load.
	if ( wp_style_is( 'themonic-fonts', 'queue' ) )
		$classes[] = 'custom-font-enabled';

	if ( ! is_multi_author() )
		$classes[] = 'single-author';

	return $classes;
}
add_filter( 'body_class', 'themonic_body_class' );

/*
 * Adjusts content_width value for full-width and single image attachment
 * templates, and when there are no active widgets in the sidebar.
 *
 * @since Iconic One 1.0
 */
function themonic_content_width() {
	if ( is_page_template( 'page-templates/full-width.php' ) || is_attachment() || ! is_active_sidebar( 'themonic-sidebar' ) ) {
		global $content_width;
		$content_width = 1040;
	}
}
add_action( 'template_redirect', 'themonic_content_width' );

/* I-c-o-n-i-c O-n-e welcome text */
if ( is_admin() && isset($_GET['activated'] ) && $pagenow ==	"themes.php" )
	wp_redirect( 'themes.php?page=iconic_one_theme_options');

require_once( get_template_directory() . '/inc/iconic-one-options.php' );


