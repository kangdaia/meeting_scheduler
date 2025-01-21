import { useEffect } from 'react';

export function DashboardLayout() {
  return (
    <div className="grid grid-cols-12 gap-4 p-6">
      {/* 요약 정보 섹션 */}
      <div className="col-span-12">
        // 요약 정보 섹션
      </div>
      
      {/* 예정된 일정 섹션 */}
      <div className="col-span-12 md:col-span-6 lg:col-span-8">
        // 예정된 일정 섹션
      </div>
      
      {/* 할 일 목록 섹션 */}
      <div className="col-span-12 md:col-span-6 lg:col-span-4">
        // 할 일 목록 섹션
      </div>
    </div>
  );
}