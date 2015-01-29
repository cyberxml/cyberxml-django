<?php

/*
 * Iconic One Customizer - visit Themonic.com
 *
 * @since Iconic One 1.0
 *
 */
function themonic_customize_register( $wp_customize ) {
	$wp_customize->get_setting( 'blogname' )->transport = 'postMessage';
	$wp_customize->get_setting( 'blogdescription' )->transport = 'postMessage';
}
add_action( 'customize_register', 'themonic_customize_register' );

/*
 * Loads Theme Customizer preview changes asynchronously.
 *
 * @since Iconic One 1.0
 */
function themonic_customize_preview_js() {
	wp_enqueue_script( 'themonic-customizer', get_template_directory_uri() . '/js/theme-customizer.js', array( 'customize-preview' ), '20130527', true );
}
add_action( 'customize_preview_init', 'themonic_customize_preview_js' );
/*
 * Sanitize functions.
 */
function iconic_one_sanitize_text( $input ) {
    return wp_kses_post( force_balance_tags( $input ) );
}
function iconic_one_sanitize_checkbox( $input ) {
    if ( $input == 1 ) {
        return 1;
    } else {
        return '';
    }
}
//Themonic customizer begins
function themonic_theme_customizer( $wp_customize ) {
     $wp_customize->add_section( 'themonic_logo_section' , array(
    'title'       => __( 'Logo', 'themonic' ),
    'priority'    => 30,
    'description' => 'Upload a logo to replace the default site name and description in the header',
) );
$wp_customize->add_setting( 'themonic_logo' , array('default' => '', 'sanitize_callback' => 'esc_url_raw',));
$wp_customize->add_control( new WP_Customize_Image_Control( $wp_customize, 'themonicl_logo', array(
    'label'    => __( 'Logo', 'themonic' ),
    'section'  => 'themonic_logo_section',
    'settings' => 'themonic_logo',
) ) );
//Footer text area
class Themonic_Textarea_Control extends WP_Customize_Control {
	public $type = 'textarea';
	public function render_content() {
?>
<label>
	<span class="customize-control-title"><?php echo esc_html( $this->label ); ?></span>
	<textarea rows="4" style="width:100%;" <?php $this->link(); ?>><?php echo esc_textarea( $this->value() ); ?></textarea>
</label>
<?php
	}
}

$wp_customize->add_section('content' , array(
	'priority'    => 200,
));
$wp_customize->add_setting('textarea_copy', array('default' => 'Copyright 2013', 'sanitize_callback' => 'iconic_one_sanitize_text',));
$wp_customize->add_control(new Themonic_Textarea_Control($wp_customize, 'textarea_copy', array(
	'label' => 'Footer Copyright',
	'section' => 'content',
	'settings' => 'textarea_copy',
)));
$wp_customize->add_section('content' , array(
	'title' => __('Footer','themonic'),
	'priority'    => 300,
));
$wp_customize->add_setting('custom_text_right', array('default' => 'Custom Text Right', 'sanitize_callback' => 'iconic_one_sanitize_text',));
$wp_customize->add_control(new Themonic_Textarea_Control($wp_customize, 'custom_text_right', array(
	'label' => 'Custom Footer Text Right',
	'section' => 'content',
	'settings' => 'custom_text_right',
)));

//social text area
class Social_Textarea_Control extends WP_Customize_Control {
	public $type = 'textarea';
	public function render_content() {
?>
<label>
	<span class="customize-control-title"><?php echo esc_html( $this->label ); ?></span>
	<textarea rows="1" style="width:100%;" <?php $this->link(); ?>><?php echo esc_textarea( $this->value() ); ?></textarea>
</label>
<?php
	}
}

$wp_customize->add_setting(
    'iconic_one_social_activate', array('default' => '', 'sanitize_callback' => 'iconic_one_sanitize_checkbox',
	));
	$wp_customize->add_control(
    'iconic_one_social_activate',
    array(
        'type' => 'checkbox',
        'label' => 'Show social buttons',
        'section' => 'sl_content',
    )
);

$wp_customize->add_section('sl_content' , array(
	'priority'    => 500,
));
$wp_customize->add_setting('twitter_url', array('default' => 'http://twitter.com/', 'sanitize_callback' => 'iconic_one_sanitize_text',));
$wp_customize->add_control(new Social_Textarea_Control($wp_customize, 'twitter_url', array(
	'label' => 'Twitter url',
	'section' => 'sl_content',
	'settings' => 'twitter_url',
)));

$wp_customize->add_section('sl_content' , array(
	'priority'    => 600,
));
$wp_customize->add_setting('facebook_url', array('default' => 'http://facebook.com/', 'sanitize_callback' => 'iconic_one_sanitize_text',));
$wp_customize->add_control(new Social_Textarea_Control($wp_customize, 'facebook_url', array(
	'label' => 'Facebook url',
	'section' => 'sl_content',
	'settings' => 'facebook_url',
)));
$wp_customize->add_section('sl_content' , array(
	'priority'    => 700,
));
$wp_customize->add_setting('plus_url', array('default' => 'http://plus.google.com/', 'sanitize_callback' => 'iconic_one_sanitize_text',));
$wp_customize->add_control(new Social_Textarea_Control($wp_customize, 'plus_url', array(
	'label' => 'Google Plus url',
	'section' => 'sl_content',
	'settings' => 'plus_url',
)));
$wp_customize->add_section('sl_content' , array(
'title' => __('Social','themonic'),
	'priority'    => 40,
));
$wp_customize->add_setting('rss_url', array('default' => 'http://wordpress.org/', 'sanitize_callback' => 'iconic_one_sanitize_text',));
$wp_customize->add_control(new Social_Textarea_Control($wp_customize, 'rss_url', array(
	'label' => 'rss url',
	'section' => 'sl_content',
	'settings' => 'rss_url',
)));
}
add_action('customize_register', 'themonic_theme_customizer');
