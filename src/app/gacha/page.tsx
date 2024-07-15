"use client";
import { useState } from 'react';

import Image from 'next/image';
import Link from 'next/link';

import GemImage from '@/assets/picture/background/gem.png';

import BtnBack from '@/assets/picture/button/btnBack.png';

import bannerAMI from '@/assets/picture/gacha/banner/banner_AMI.png';
import bannerAshyra from '@/assets/picture/gacha/banner/banner_Ashyra.png';
import bannerDebirun from '@/assets/picture/gacha/banner/banner_Debirun.png';
import bannerMildR from '@/assets/picture/gacha/banner/banner_Mild-R.png';
import bannerTsururu from '@/assets/picture/gacha/banner/banner_Tsururu.png';
import bannerXonebu from '@/assets/picture/gacha/banner/banner_Xonebu.png';

type GachaChar = "AMI" | "Ashyra" | "Debirun" | "Mild-R" | "Tsururu" | "Xonebu";

export default function GachaPage() {
    const [nowChar, setNowChar] = useState<GachaChar>("AMI");

    const handleChangeChar = (char: GachaChar) => setNowChar(char);

    return (
        <main className="p-4 flex flex-col h-full">
            <div className="flex justify-between">
                <div className="flex flex-row items-center">
                    <Link href="/">
                        <Image src={BtnBack} alt="logo" width={64} />
                    </Link>
                </div>

                <div className="flex flex-row flex-1 w-full items-center justify-end gap-4">
                    <div className="relative w-[190px] bg-[#99d9ea] h-8 rounded-md flex justify-end items-center p-4">
                        <Image src={GemImage} alt="logo" width={64} className="absolute left-0" />
                        <span className="text-lg mr-4">999,999</span>
                    </div>
                </div>
            </div>

            <div className="h-[calc(100%-72px)] grid grid-cols-3 pt-4 gap-2">
                <div className="col-span-1 overflow-auto max-h-full flex flex-col gap-4">
                    <Image src={bannerAMI} alt="logo" className="w-full" onClick={() => handleChangeChar("AMI")} />
                    <Image src={bannerAshyra} alt="logo" className="w-full" onClick={() => handleChangeChar("Ashyra")} />
                    <Image src={bannerDebirun} alt="logo" className="w-full" onClick={() => handleChangeChar("Debirun")} />
                    <Image src={bannerMildR} alt="logo" className="w-full" onClick={() => handleChangeChar("Mild-R")} />
                    <Image src={bannerTsururu} alt="logo" className="w-full" onClick={() => handleChangeChar("Tsururu")} />
                    <Image src={bannerXonebu} alt="logo" className="w-full" onClick={() => handleChangeChar("Xonebu")} />
                </div>

                <div className="col-span-2 flex flex-col gap-2">
                    <div className="w-full h-5/6 flex items-center justify-center">
                        <span className="text-4xl">กดเพื่อสุ่มตู้ Rate-Up {nowChar} ได้เลย!!!</span>
                    </div>
                    <div className="w-full h-1/6 flex flex-row justify-end items-center gap-4">
                        <button className="bg-[#00ff00] text-white px-4 py-3 text-xl rounded-full">สุ่ม 142 Gem</button>
                        <button className="bg-[#00ff00] text-white px-4 py-3 text-xl rounded-full">สุ่ม 1420 Gem</button>
                    </div>
                </div>
            </div>
        </main>
    )
}