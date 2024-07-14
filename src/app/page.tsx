"use client";
import Image from "next/image";
import Link from "next/link";

import GemImage from "@/assets/picture/background/gem.png";
import BtnSetting from "@/assets/picture/button/btnSetting.png";

import BtnPlay from "@/assets/picture/button/btnPlay.png";
import BtnGacha from "@/assets/picture/button/btnGacha.png";

export default function Home() {
  return (
    <main className="p-4 flex flex-col justify-between h-full">
      <div className="flex justify-between">
        <div>
          <h1 className="text-4xl">142 Game</h1>
          <span className="text-lg ml-2">ver 0.0.1</span>
        </div>

        <div className="flex flex-row flex-1 w-full items-center justify-end gap-4">
          <div className="relative w-[190px] bg-[#99d9ea] h-8 rounded-md flex justify-end items-center p-4">
            <Image src={GemImage} alt="logo" width={64} className="absolute left-0" />
            <span className="text-lg mr-4">999,999</span>
          </div>

          <Image src={BtnSetting} alt="logo" width={64} />
        </div>
      </div>

      <div className="flex flex-col items-end justify-center">
        <Link href="/gacha">
          <Image src={BtnGacha} alt="logo" width={128} />
        </Link>

        <Link href="/game">
          <Image src={BtnPlay} alt="logo" width={128} />
        </Link>
      </div>
    </main>
  );
}
