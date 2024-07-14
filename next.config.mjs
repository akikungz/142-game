/** @type {import('next').NextConfig} */
const nextConfig = {
    output: 'export',
    distDir: 'dist',
    images: {
        unoptimized: true,
    },
    experimental: {
        missingSuspenseWithCSRBailout: false,
    }
};

export default nextConfig;
