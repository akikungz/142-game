/** @type {import('next').NextConfig} */
const nextConfig = {
    output: 'export',
    distDir: 'dist',
    images: {
        unoptimized: true,
    },
    experimental: {
        missingSuspenseWithCSRBailout: false,
    },
    basePath: '/142-game'
};

export default nextConfig;
